from src.schema import Trajectory

def test_trajectory_serializes():
    t = Trajectory(
        id="test-1", category="clean", task_id="t1",
        task_description="test", attack_payload=None,
        turns=[{"role": "user", "content": "hi"}],
        final_action="did nothing", compromised=False,
        severity="none", rationale="control case",
        labeler="auto_checker", label_method="automated",
    )
    assert '"category": "clean"' in t.to_json()