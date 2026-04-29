from datetime import datetime

def transform_github_events(raw_data: list) -> dict:
    """
    Transforms raw, noisy 3rd party API data into a clean, normalized format.
    Example specific to GitHub public events.
    """
    processed_records = []
    
    for event in raw_data:
        if event.get('type') == 'PushEvent':
            processed_records.append({
                "actor": event.get('actor', {}).get('login'),
                "repo": event.get('repo', {}).get('name'),
                "timestamp": event.get('created_at'),
                "commit_count": len(event.get('payload', {}).get('commits', []))
            })
            
    summary = {
        "processed_at": datetime.utcnow().isoformat(),
        "total_push_events": len(processed_records),
        "data": processed_records
    }
    
    return summary
