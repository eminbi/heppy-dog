import matplotlib.pyplot as plt

def visualize_results(data_path):
    data = pd.read_csv(data_path)
    plt.figure(figsize=(10,6))
    plt.plot(data['time'], data['emotion_signal'])
    plt.title("Emotion Signal Over Time")
    plt.xlabel("Time")
    plt.ylabel("Emotion Signal")
    plt.show()

if __name__ == "__main__":
    visualize_results("improved_emotion_behavior_signal.csv")
