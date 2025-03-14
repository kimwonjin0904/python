import ollama
import logging
from tkinter import *
from tkinter import scrolledtext

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Ollama 모델 설정
model_name = "mistral"

# 대화 기록 유지
messages = [{"role": "system", "content": "너는 친절한 AI 비서야. 짧고 간결하게 대답해줘."}]

def send_message(event=None):
    """사용자가 입력한 메시지를 채팅창에 추가하고 Ollama에게 요청"""
    message = entry.get().strip()
    if not message:
        return  # 빈 입력 방지

    # 사용자 메시지 출력
    chat_window.config(state=NORMAL)
    chat_window.insert(END, f"\nYOU: {message}\n", "user")
    chat_window.config(state=DISABLED)
    chat_window.yview(END)  # 자동 스크롤
    entry.delete(0, END)  # 입력 필드 초기화

    # Ollama API 호출
    try:
        messages.append({"role": "user", "content": message})
        response = ollama.chat(model=model_name, messages=messages)
        ai_reply = response['message']['content']

        # AI 응답 출력
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"AI: {ai_reply}\n", "ai")
        chat_window.config(state=DISABLED)
        chat_window.yview(END)

        # 대화 기록 유지
        messages.append({"role": "assistant", "content": ai_reply})

        logging.info(f"Ollama 응답: {ai_reply}")

    except Exception as e:
        logging.error(f"Ollama 오류: {e}")

# GUI 생성
app = Tk()
app.title("Chat UI")
app.geometry("400x500")

# 채팅 창
chat_window = scrolledtext.ScrolledText(app, wrap=WORD, state=DISABLED, height=20, width=50)
chat_window.pack(pady=10, padx=10, expand=True, fill=BOTH)

# 입력 프레임
input_frame = Frame(app)
input_frame.pack(pady=10, padx=10, fill=X)

# 입력 필드
entry = Entry(input_frame)
entry.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
entry.bind("<Return>", send_message)  # 엔터 키로 전송 가능

# 전송 버튼
btn = Button(input_frame, text="Send", command=send_message)
btn.pack(side=RIGHT, padx=5, pady=5)

app.mainloop()
