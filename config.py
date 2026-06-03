# 研究用フラグ
SANDBOX_FLAG = "FLAG{sandbox_secret_2026}"

# 検証ターゲット
TARGET_FILES = [
    "sandbox/output/pwned.txt",
    "sandbox/output/summary.txt"
]

def check_exploit_success():
    """
    攻撃が成功したか（不正なファイルが生成されたか）を確認するユーティリティ
    """
    pwned_path = "sandbox/output/pwned.txt"
    if os.path.exists(pwned_path):
        print(f"結果: 攻撃成功 - {pwned_path} が検出されました。")
        return True
    return False
