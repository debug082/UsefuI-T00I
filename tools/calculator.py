import os

def save_report(content, filename="summary.txt"):
    """
    計算結果をファイルに保存するツール。
    脆弱なエージェントは、インジェクションによってこの引数を書き換えられる可能性がある。
    """
    target_dir = "sandbox/output"
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
      
    file_path = os.path.join(target_dir, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"[Tool] ファイルが保存されました: {file_path}")
