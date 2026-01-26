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
        "tag_name": "v1.1.0",
        "name": "v1.1.0 - O-Award Visualization Engine",
        "body": "## Major Update: Visualization Engine & O-Award Analysis\n\nThis release introduces a comprehensive visualization system based on the analysis of 30 Outstanding Winner (O-Award) papers from 2020-2024.\n\n### New Features\n\n#### 1. Visualization Templates (`templates/visualization/`)\n- **Professional Style**: `mcm_style.mplstyle` for publication-quality matplotlib figures (Okabe-Ito color palette, 300 DPI).\n- **Core Plot Templates**:\n  - `phase_portrait.py`: Phase plane analysis for ODEs (Type A).\n  - `time_series.py`: Forecasts with confidence intervals (Type A/C).\n  - `network_graph.py`: Topology and hierarchy visualizations (Type B/D/F).\n  - `heatmap.py`: Correlation matrices and spatial heatmaps (Type C/E).\n  - `multi_panel.py`: Automated (a)(b) subplot layouts.\n\n#### 2. Deep Analysis Reports (`references/analysis_data/`)\n- Detailed visualization analysis for **Problem Types A through F**.\n- `visualization_findings.md`: Summary of 'Golden Rules' for MCM figures.\n- Extracted from 30+ actual O-award papers.\n\n#### 3. Documentation\n- `visualization-guide.md`: Guide on selecting the right chart for your problem type.\n- Updated `SKILL.md` with a new **Visualization Phase** in the workflow.",
        "draft": False,
        "prerelease": False
    }
    
    print("\n🚀 Creating Release v1.1.0...")
    
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
