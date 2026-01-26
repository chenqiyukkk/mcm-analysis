from composio import Composio
import sys

# Initialize
toolset = Composio(api_key="ak_M6CgOkAiyxhDSH4CzADi")
entity_id = "chenqiyu"
entity = toolset.get_entity(id=entity_id)

print(f"Checking GitHub connection for user: {entity_id}...")

try:
    # Check if connected using string "GITHUB"
    connections = entity.get_connections(app="GITHUB")
    
    if not connections:
        print("❌ GitHub not connected.")
        print("Initiating connection request...")
        # Use string "GITHUB"
        connection_request = entity.initiate_connection(app_name="GITHUB")
        print(f"\n👉 Please open this URL to authorize GitHub: {connection_request.redirectUrl}")
        print("\nAfter authorizing, re-run this script.")
        sys.exit(1)
        
    print("✅ GitHub is connected!")
    
    release_payload = {
        "owner": "chenqiyukkk",
        "repo": "mcm-analysis",
        "tag_name": "v1.1.1",
        "name": "v1.1.1 - Self-Evolution & New Models",
        "body": "## Feature Update: Self-Evolution Mechanism\n\nThis release introduces the **Self-Evolution Mode**, allowing the skill to autonomously learn and update its knowledge base from user interactions.\n\n### New Features\n\n#### 1. Self-Evolution (`scripts/auto_evolve.py`)\n- **Autonomous Learning**: Automatically extracts new models and insights from sessions.\n- **Self-Update**: Commits and pushes new knowledge to the repository.\n\n#### 2. Model Library Expansion (`references/models-library.md`)\n- Added **10+ new models** derived from 2022-2023 O-Award papers.\n- Updated usage guidance for modern competition trends.\n\n### Improvements\n- Fixed version synchronization issues.\n- Enhanced documentation for the evolution workflow.",
        "draft": False,
        "prerelease": False
    }
    
    print("\n🚀 Creating Release v1.1.1...")
    
    # Execute Action using string ID
    response = toolset.execute_action(
        action="GITHUB_CREATE_A_RELEASE",
        params=release_payload,
        entity_id=entity_id
    )
    
    print("Response:", response)
    print("\n✅ Release published successfully!")

except Exception as e:
    print(f"\n❌ Error occurred: {e}")
