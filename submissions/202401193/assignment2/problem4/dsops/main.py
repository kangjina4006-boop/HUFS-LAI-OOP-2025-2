if __name__ == "__main__":
    from . import train_test_split, label_distribution

    print("--- dsops 패키지 데모 시작 ---")
    
    print("\n[1. train_test_split 기본 테스트]")
    seq_data = list(range(10))
    test_ratio = 0.4
    
    tr, te = train_test_split(seq_data, test_ratio, seed=42) 
    print(f"원본 데이터: {seq_data}")
    print(f"테스트 비율: {test_ratio}")
    print(f"Train set (60%): {tr}")
    print(f"Test set (40%): {te}")
    print(f"전체 길이 확인: {len(tr) + len(te)}")
    
    print("\n[2. label_distribution 테스트]")
    labels = ["cat", "dog", "cat", "fish", "dog", "cat", "dog"]
    distribution = label_distribution(labels)
    print(f"레이블: {labels}")
    print(f"분포 결과: {distribution}")
    
    print("\n[3. 엣지 케이스 테스트]")
    
    tr_all, te_all = train_test_split(seq_data, 1.0)
    print(f"비율 1.0 -> Train: {tr_all}, Test: {te_all}")

    tr_none, te_none = train_test_split(seq_data, 0.0)
    print(f"비율 0.0 -> Train: {tr_none}, Test: {te_none}")

    tr_empty, te_empty = train_test_split([], 0.3)
    print(f"빈 입력 -> Train: {tr_empty}, Test: {te_empty}")

    print("\n[ValueError 테스트]")
    try:
        train_test_split(seq_data, 1.1)
    except ValueError as e:
        print(f"비율 1.1에서 ValueError 포착: {e}")
        
    try:
        train_test_split(seq_data, -0.1)
    except ValueError as e:
        print(f"비율 -0.1에서 ValueError 포착: {e}")
        
    print("\n--- dsops 데모 완료 ---")
