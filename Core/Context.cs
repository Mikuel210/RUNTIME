namespace Core;

public class Context(Source source, Context? parentContext = null, Position? parentStartPosition = null) {

	public Source Source { get; } = source;
	public Context? ParentContext { get; } = parentContext;
	public Position? ParentStartPosition { get; } = parentStartPosition;

}