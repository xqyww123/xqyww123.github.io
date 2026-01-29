#!/usr/bin/env python3
"""
Analyze authors who published as first author in both POPL and ICLR in the past decade (2016-2025)
Data source: DBLP API

Note: Starting from 2018, POPL papers are published in PACMPL (Proceedings of the ACM on Programming Languages) journal
"""

import requests
import time
from collections import defaultdict
from typing import Dict, List, Tuple

# DBLP API base URL
DBLP_API_BASE = "https://dblp.org/search/publ/api"

# Year range
START_YEAR = 2016
END_YEAR = 2025


def fetch_dblp_by_toc(toc_key: str) -> List[dict]:
    """
    Fetch publication list via TOC (Table of Contents) key
    This is a more precise query method
    """
    publications = []
    hits_per_page = 1000
    first = 0

    while True:
        query = f"toc:{toc_key}:"
        params = {
            "q": query,
            "format": "json",
            "h": hits_per_page,
            "f": first
        }

        try:
            response = requests.get(DBLP_API_BASE, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            result = data.get("result", {})
            hits = result.get("hits", {})
            total = int(hits.get("@total", 0))
            hit_list = hits.get("hit", [])

            if not hit_list:
                break

            for hit in hit_list:
                info = hit.get("info", {})
                publications.append(info)

            first += hits_per_page
            if first >= total:
                break

            time.sleep(0.3)

        except Exception as e:
            print(f"  Error fetching data for {toc_key}: {e}")
            break

    return publications


def fetch_dblp_by_stream(stream_key: str, year: int) -> List[dict]:
    """
    Fetch publication list via stream key and year
    """
    publications = []
    hits_per_page = 1000
    first = 0

    while True:
        query = f"stream:{stream_key}: year:{year}"
        params = {
            "q": query,
            "format": "json",
            "h": hits_per_page,
            "f": first
        }

        try:
            response = requests.get(DBLP_API_BASE, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            result = data.get("result", {})
            hits = result.get("hits", {})
            total = int(hits.get("@total", 0))
            hit_list = hits.get("hit", [])

            if not hit_list:
                break

            for hit in hit_list:
                info = hit.get("info", {})
                publications.append(info)

            first += hits_per_page
            if first >= total:
                break

            time.sleep(0.3)

        except Exception as e:
            print(f"  Error fetching data for stream:{stream_key} year:{year}: {e}")
            break

    return publications


def extract_first_author(publication: dict) -> Tuple[str | None, str | None]:
    """
    Extract first author from publication information
    Returns (author name, author DBLP ID/URL)
    """
    authors = publication.get("authors", {}).get("author", [])

    # Handle single author case (DBLP may return dict instead of list)
    if isinstance(authors, dict):
        authors = [authors]

    if not authors:
        return None, None

    first_author = authors[0]

    # Author can be either string or dict
    if isinstance(first_author, str):
        return first_author, None
    elif isinstance(first_author, dict):
        name = first_author.get("text", first_author.get("@pid", ""))
        pid = first_author.get("@pid", "")
        return name, pid
    
    return None, None


def normalize_author_name(name: str) -> str:
    """
    Normalize author name for comparison
    """
    if not name:
        return ""
    # Convert to lowercase and remove extra spaces
    return " ".join(name.lower().split())


def is_popl_paper(publication: dict) -> bool:
    """
    Check if it's a POPL paper
    For PACMPL, check if the number field is POPL
    """
    venue = publication.get("venue", "")
    number = publication.get("number", "")

    # Direct POPL conference
    if "POPL" in venue and "PACMPL" not in venue and "@" not in venue:
        return True

    # POPL papers in PACMPL journal
    if "Proc. ACM Program. Lang" in venue or "PACMPL" in venue:
        if number == "POPL":
            return True
    
    return False


def fetch_popl_data() -> Dict[str, List[dict]]:
    """
    Fetch all POPL data from the past decade
    """
    author_papers = defaultdict(list)

    print("\nFetching POPL data...")

    # Use stream query
    for year in range(START_YEAR, END_YEAR + 1):
        print(f"  {year}...", end=" ", flush=True)

        # Try stream query for conf/popl
        pubs = fetch_dblp_by_stream("conf/popl", year)

        # Filter out genuine POPL papers (exclude workshops, etc.)
        popl_pubs = []
        for pub in pubs:
            venue = pub.get("venue", "")
            pub_type = pub.get("type", "")
            # Exclude workshops, editorship, etc.
            if "@" not in venue and pub_type not in ["Editorship"]:
                popl_pubs.append(pub)

        # If stream query returns nothing, try querying PACMPL
        if not popl_pubs and year >= 2018:
            # PACMPL volume mapping:
            # POPL 2018 -> vol 2, POPL 2019 -> vol 3, etc.
            vol = year - 2016
            toc_key = f"db/journals/pacmpl/pacmpl{vol}.bht"
            all_pacmpl = fetch_dblp_by_toc(toc_key)

            for pub in all_pacmpl:
                if is_popl_paper(pub):
                    popl_pubs.append(pub)

        print(f"Found {len(popl_pubs)} papers")
        
        for pub in popl_pubs:
            first_author, pid = extract_first_author(pub)
            if first_author:
                title = pub.get("title", "Unknown")
                normalized = normalize_author_name(first_author)
                key = pid if pid else normalized
                author_papers[key].append({
                    "year": year,
                    "title": title,
                    "author_name": first_author,
                    "normalized_name": normalized,
                    "pid": pid,
                    "venue": "POPL"
                })
        
        time.sleep(0.5)
    
    return author_papers


def fetch_iclr_data() -> Dict[str, List[dict]]:
    """
    Fetch all ICLR data from the past decade
    """
    author_papers = defaultdict(list)

    print("\nFetching ICLR data...")

    for year in range(START_YEAR, END_YEAR + 1):
        print(f"  {year}...", end=" ", flush=True)

        pubs = fetch_dblp_by_stream("conf/iclr", year)

        # Filter out main conference papers (exclude workshops, tiny papers, etc.)
        iclr_pubs = []
        for pub in pubs:
            venue = pub.get("venue", "")
            key = pub.get("key", "")
            pub_type = pub.get("type", "")

            # Only keep main conference papers
            if pub_type == "Editorship":
                continue
            # Exclude workshops (key usually contains special markers)
            if "conf/iclr/" in key:
                # Main conference paper keys are usually in format conf/iclr/AuthorYY
                # Workshop papers usually have additional markers
                key_parts = key.split("/")
                if len(key_parts) == 3:
                    # Check if it's a workshop
                    if "w" not in key_parts[2][:4].lower() or key_parts[2][0].isupper():
                        iclr_pubs.append(pub)

        # Simpler filter: only venue is ICLR and doesn't contain special markers
        iclr_pubs = [p for p in pubs
                     if p.get("type") != "Editorship"
                     and "Workshop" not in p.get("venue", "")
                     and "Tiny" not in p.get("venue", "")]

        print(f"Found {len(iclr_pubs)} papers")
        
        for pub in iclr_pubs:
            first_author, pid = extract_first_author(pub)
            if first_author:
                title = pub.get("title", "Unknown")
                normalized = normalize_author_name(first_author)
                key = pid if pid else normalized
                author_papers[key].append({
                    "year": year,
                    "title": title,
                    "author_name": first_author,
                    "normalized_name": normalized,
                    "pid": pid,
                    "venue": "ICLR"
                })
        
        time.sleep(0.5)
    
    return author_papers


def find_common_authors(popl_authors: Dict, iclr_authors: Dict) -> List[dict]:
    """
    Find authors who published as first author in both conferences
    """
    common = []

    popl_keys = set(popl_authors.keys())
    iclr_keys = set(iclr_authors.keys())

    # Find intersection based on key (pid or normalized name)
    intersection = popl_keys & iclr_keys

    for key in intersection:
        popl_papers = popl_authors[key]
        iclr_papers = iclr_authors[key]

        # Get representative name
        name = popl_papers[0]["author_name"]

        common.append({
            "key": key,
            "name": name,
            "popl_papers": popl_papers,
            "iclr_papers": iclr_papers,
            "popl_count": len(popl_papers),
            "iclr_count": len(iclr_papers)
        })

    # Sort by total paper count
    common.sort(key=lambda x: (x["popl_count"] + x["iclr_count"]), reverse=True)
    
    return common


def print_results(common_authors: List[dict], popl_count: int, iclr_count: int):
    """
    Print results
    """
    print("\n" + "="*80)
    print(f"Authors who published as first author in both POPL and ICLR in the past decade ({START_YEAR}-{END_YEAR})")
    print("="*80)

    print(f"\nStatistics:")
    print(f"  Total POPL first authors: {popl_count}")
    print(f"  Total ICLR first authors: {iclr_count}")
    print(f"  Common authors: {len(common_authors)}")

    if not common_authors:
        print("\nNo authors found who published as first author in both conferences.")
        return

    print(f"\nDetailed list:\n")

    for i, author in enumerate(common_authors, 1):
        print(f"\n{i}. {author['name']}")
        print(f"   DBLP PID: {author['key']}")
        print(f"   POPL first author papers ({author['popl_count']} papers):")
        for paper in sorted(author['popl_papers'], key=lambda x: x['year']):
            print(f"      [{paper['year']}] {paper['title']}")
        print(f"   ICLR first author papers ({author['iclr_count']} papers):")
        for paper in sorted(author['iclr_papers'], key=lambda x: x['year']):
            print(f"      [{paper['year']}] {paper['title']}")

    print("\n" + "="*80)
    print(f"Total: {len(common_authors)} authors")
    print("="*80)


def main():
    print("="*80)
    print("Analysis of First Author Intersection between POPL and ICLR")
    print(f"Time range: {START_YEAR} - {END_YEAR}")
    print("="*80)

    # Fetch POPL data
    popl_authors = fetch_popl_data()
    popl_count = len(popl_authors)
    print(f"\nPOPL has {popl_count} distinct first authors")

    # Fetch ICLR data
    iclr_authors = fetch_iclr_data()
    iclr_count = len(iclr_authors)
    print(f"\nICLR has {iclr_count} distinct first authors")

    # Find intersection
    common = find_common_authors(popl_authors, iclr_authors)

    # Print results
    print_results(common, popl_count, iclr_count)

    # Save to file
    output_file = "common_authors_result.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Analysis of First Author Intersection between POPL and ICLR\n")
        f.write(f"Authors with the same name may exist!\n")
        f.write(f"Time range: {START_YEAR} - {END_YEAR}\n")
        f.write(f"="*60 + "\n\n")
        f.write(f"Statistics:\n")
        f.write(f"  POPL first authors: {popl_count}\n")
        f.write(f"  ICLR first authors: {iclr_count}\n")
        f.write(f"  Common authors: {len(common)}\n\n")

        if common:
            f.write(f"Detailed list:\n")
            f.write(f"="*60 + "\n")

            for i, author in enumerate(common, 1):
                f.write(f"\n{i}. {author['name']}\n")
                f.write(f"   DBLP PID: {author['key']}\n")
                f.write(f"   POPL ({author['popl_count']} papers):\n")
                for paper in sorted(author['popl_papers'], key=lambda x: x['year']):
                    f.write(f"      [{paper['year']}] {paper['title']}\n")
                f.write(f"   ICLR ({author['iclr_count']} papers):\n")
                for paper in sorted(author['iclr_papers'], key=lambda x: x['year']):
                    f.write(f"      [{paper['year']}] {paper['title']}\n")

    print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()
