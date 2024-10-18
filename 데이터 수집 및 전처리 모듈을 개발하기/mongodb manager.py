from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, db_name="pet_behavior_db", collection_name="behaviors"):
        """
        MongoDB 초기화 및 연결 생성
        Args:
        - db_name: 데이터베이스 이름
        - collection_name: 컬렉션 이름
        """
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_behavior(self, behavior, confidence):
        """
        행동 데이터를 MongoDB에 저장하는 함수
        Args:
        - behavior: 예측된 행동 (텍스트)
        - confidence: 행동 예측에 대한 신뢰도 (실수)
        """
        behavior_data = {
            "behavior": behavior,
            "confidence": confidence,
            "timestamp": datetime.datetime.now()
        }
        result = self.collection.insert_one(behavior_data)
        print(f"데이터가 저장되었습니다. ObjectId: {result.inserted_id}")

    def fetch_behaviors(self):
        """
        저장된 행동 데이터를 조회하는 함수
        Returns:
        - 저장된 행동 데이터 리스트
        """
        return list(self.collection.find())

    def close(self):
        """
        MongoDB 연결을 닫는 함수
        """
        self.client.close()
        print("MongoDB 연결이 종료되었습니다.")

if __name__ == "__main__":
    # 예시 사용법
    mongo_manager = MongoDBManager()

    # 새로운 행동 데이터 저장
    mongo_manager.save_behavior("jumping", 0.92)

    # 저장된 데이터 조회
    behaviors = mongo_manager.fetch_behaviors()
    for behavior in behaviors:
        print(behavior)

    # MongoDB 연결 종료
    mongo_manager.close()
