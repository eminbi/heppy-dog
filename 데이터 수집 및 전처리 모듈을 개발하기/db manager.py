import sqlite3
import os

class DBManager:
    def __init__(self, db_path="pet_behavior.db"):
        """
        데이터베이스 초기화 및 연결 생성
        Args:
        - db_path: 데이터베이스 파일 경로
        """
        self.db_path = db_path
        self.conn = None
        self.connect()

    def connect(self):
        """
        데이터베이스에 연결하는 함수
        """
        if not os.path.exists(self.db_path):
            print(f"데이터베이스 파일이 존재하지 않으므로 새로 생성합니다: {self.db_path}")
        try:
            self.conn = sqlite3.connect(self.db_path)
            print(f"데이터베이스에 연결되었습니다: {self.db_path}")
            self.create_table()
        except sqlite3.Error as e:
            print(f"데이터베이스 연결 실패: {e}")

    def create_table(self):
        """
        행동 데이터를 저장할 테이블 생성
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS pet_behavior (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            behavior TEXT NOT NULL,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
            print("테이블이 성공적으로 생성되었습니다.")
        except sqlite3.Error as e:
            print(f"테이블 생성 실패: {e}")

    def save_behavior(self, behavior, confidence):
        """
        행동 데이터를 테이블에 저장하는 함수
        Args:
        - behavior: 예측된 행동 (텍스트)
        - confidence: 행동 예측에 대한 신뢰도 (실수)
        """
        insert_sql = "INSERT INTO pet_behavior (behavior, confidence) VALUES (?, ?);"
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_sql, (behavior, confidence))
            self.conn.commit()
            print(f"행동 데이터가 성공적으로 저장되었습니다: {behavior} ({confidence})")
        except sqlite3.Error as e:
            print(f"데이터 저장 실패: {e}")

    def fetch_behaviors(self):
        """
        저장된 행동 데이터를 조회하는 함수
        Returns:
        - 저장된 행동 데이터 리스트
        """
        fetch_sql = "SELECT * FROM pet_behavior;"
        try:
            cursor = self.conn.cursor()
            cursor.execute(fetch_sql)
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"데이터 조회 실패: {e}")
            return []

    def close(self):
        """
        데이터베이스 연결을 닫는 함수
        """
        if self.conn:
            self.conn.close()
            print("데이터베이스 연결이 종료되었습니다.")

if __name__ == "__main__":
    # 예시 사용법
    db_manager = DBManager()

    # 새로운 행동 데이터 저장
    db_manager.save_behavior("jumping", 0.92)

    # 저장된 데이터 조회
    behaviors = db_manager.fetch_behaviors()
    for behavior in behaviors:
        print(behavior)

    # 데이터베이스 연결 종료
    db_manager.close()
