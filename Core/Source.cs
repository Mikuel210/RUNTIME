namespace Core;

public class Source(string name, string text) {

	public string Name { get; set; } = name;

	private string _text = text;
	public string Text {
		get => _text;

		private set {
			_text = value;
			OnTextChanged?.Invoke();
		}
	}

	public delegate void TextPrependEvent(int characterCount);
	public event TextPrependEvent? OnTextPrepend;

	public event Action? OnTextChanged;

	public void PrependText(string text) {
		OnTextPrepend?.Invoke(text.Length);
		Text = text + Text;
	}
	public void AppendText(string text) => Text += text;

}