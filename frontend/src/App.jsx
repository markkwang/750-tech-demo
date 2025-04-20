import React, { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [hasStarted, setHasStarted] = useState(false);

  const bottomRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    inputRef.current?.focus();
  }, [messages]);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleSend = async () => {
    if (!input.trim()) return;

    if (!hasStarted) setHasStarted(true);

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      // const endpoint = hasStarted ? "/messages_to_gpt" : "/summarise_web"; // Switch based on first message
      const res = await fetch(`http://localhost:5321/messages_to_gpt`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      const fullText = data.response;
      const newIndex = messages.length + 1;

      // Add empty assistant message
      setMessages((prev) => [...prev, { role: "assistant", content: "" }]);

      // Switch endpoint after first send

      // Simulate typing
      let i = 0;
      const interval = setInterval(() => {
        setMessages((prev) => {
          const updated = [...prev];
          updated[newIndex] = {
            role: "assistant",
            content: fullText.slice(0, i + 1),
          };
          return updated;
        });
        i++;
        if (i === fullText.length) {
          clearInterval(interval);
          setLoading(false);
        }
      }, 10);
    } catch (err) {
      console.error("Error talking to backend:", err);
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") handleSend();
  };

  return (
    <div className="chat-container">
      <div className="top-bar">
        <h2>🧠 GPT Chat</h2>
      </div>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <strong>{msg.role === "user" ? "You" : "GPT"}:</strong>{" "}
            {msg.content}
          </div>
        ))}
        {loading && messages[messages.length - 1]?.role !== "assistant" && (
          <div className="message assistant">GPT is typing...</div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="input-area">
        <input
          ref={inputRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={hasStarted ? "Type a message..." : "Type in a URL..."}
          autoFocus
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default App;
