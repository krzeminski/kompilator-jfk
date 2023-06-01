// Generated from c:\Users\Admin\Desktop\Nowy folder\kompilator-jfk\grammar\Dallas.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DallasLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		AND=1, OR=2, XOR=3, EQ=4, ASSIGN=5, COMMA=6, SEMI=7, LPAREN=8, RPAREN=9, 
		LCURLY=10, RCURLY=11, LBRACK=12, RBRACK=13, INT_KEY=14, FLOAT_KEY=15, 
		FLOAT_32_KEY=16, FLOAT_64_KEY=17, STRING_KEY=18, FLOAT=19, INT=20, STRING=21, 
		PLUS=22, MINUS=23, ASTERISK=24, SLASH=25, DOT=26, EXCLAMATION=27, DQ=28, 
		ID=29, WS=30;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"AND", "OR", "XOR", "EQ", "ASSIGN", "COMMA", "SEMI", "LPAREN", "RPAREN", 
			"LCURLY", "RCURLY", "LBRACK", "RBRACK", "INT_KEY", "FLOAT_KEY", "FLOAT_32_KEY", 
			"FLOAT_64_KEY", "STRING_KEY", "FLOAT", "INT", "STRING", "PLUS", "MINUS", 
			"ASTERISK", "SLASH", "DOT", "EXCLAMATION", "DQ", "ID", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'&&'", "'||'", "'^^'", "'=='", "'='", "','", "';'", "'('", "')'", 
			"'{'", "'}'", "'['", "']'", "'int'", "'float'", "'float32'", "'float64'", 
			"'string'", null, null, null, "'+'", "'-'", "'*'", "'/'", "'.'", "'!'", 
			"'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "AND", "OR", "XOR", "EQ", "ASSIGN", "COMMA", "SEMI", "LPAREN", 
			"RPAREN", "LCURLY", "RCURLY", "LBRACK", "RBRACK", "INT_KEY", "FLOAT_KEY", 
			"FLOAT_32_KEY", "FLOAT_64_KEY", "STRING_KEY", "FLOAT", "INT", "STRING", 
			"PLUS", "MINUS", "ASTERISK", "SLASH", "DOT", "EXCLAMATION", "DQ", "ID", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public DallasLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Dallas.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 \u00ac\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t"+
		"\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\24\3\24\3\24\3\24\3\25\6\25\u0084\n\25\r\25\16\25\u0085\3\26\3\26\7"+
		"\26\u008a\n\26\f\26\16\26\u008d\13\26\3\26\3\26\3\27\3\27\3\30\3\30\3"+
		"\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\7\36\u00a1"+
		"\n\36\f\36\16\36\u00a4\13\36\3\37\6\37\u00a7\n\37\r\37\16\37\u00a8\3\37"+
		"\3\37\2\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= \3\2\7\3\2\62;\5\2\f\f\17\17$$\5\2C\\aac|\6\2\62;C\\aac|"+
		"\5\2\13\f\16\17\"\"\2\u00af\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3"+
		"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2"+
		"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37"+
		"\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3"+
		"\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2"+
		"\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\3?\3\2\2\2\5B\3\2\2\2\7E"+
		"\3\2\2\2\tH\3\2\2\2\13K\3\2\2\2\rM\3\2\2\2\17O\3\2\2\2\21Q\3\2\2\2\23"+
		"S\3\2\2\2\25U\3\2\2\2\27W\3\2\2\2\31Y\3\2\2\2\33[\3\2\2\2\35]\3\2\2\2"+
		"\37a\3\2\2\2!g\3\2\2\2#o\3\2\2\2%w\3\2\2\2\'~\3\2\2\2)\u0083\3\2\2\2+"+
		"\u0087\3\2\2\2-\u0090\3\2\2\2/\u0092\3\2\2\2\61\u0094\3\2\2\2\63\u0096"+
		"\3\2\2\2\65\u0098\3\2\2\2\67\u009a\3\2\2\29\u009c\3\2\2\2;\u009e\3\2\2"+
		"\2=\u00a6\3\2\2\2?@\7(\2\2@A\7(\2\2A\4\3\2\2\2BC\7~\2\2CD\7~\2\2D\6\3"+
		"\2\2\2EF\7`\2\2FG\7`\2\2G\b\3\2\2\2HI\7?\2\2IJ\7?\2\2J\n\3\2\2\2KL\7?"+
		"\2\2L\f\3\2\2\2MN\7.\2\2N\16\3\2\2\2OP\7=\2\2P\20\3\2\2\2QR\7*\2\2R\22"+
		"\3\2\2\2ST\7+\2\2T\24\3\2\2\2UV\7}\2\2V\26\3\2\2\2WX\7\177\2\2X\30\3\2"+
		"\2\2YZ\7]\2\2Z\32\3\2\2\2[\\\7_\2\2\\\34\3\2\2\2]^\7k\2\2^_\7p\2\2_`\7"+
		"v\2\2`\36\3\2\2\2ab\7h\2\2bc\7n\2\2cd\7q\2\2de\7c\2\2ef\7v\2\2f \3\2\2"+
		"\2gh\7h\2\2hi\7n\2\2ij\7q\2\2jk\7c\2\2kl\7v\2\2lm\7\65\2\2mn\7\64\2\2"+
		"n\"\3\2\2\2op\7h\2\2pq\7n\2\2qr\7q\2\2rs\7c\2\2st\7v\2\2tu\78\2\2uv\7"+
		"\66\2\2v$\3\2\2\2wx\7u\2\2xy\7v\2\2yz\7t\2\2z{\7k\2\2{|\7p\2\2|}\7i\2"+
		"\2}&\3\2\2\2~\177\5)\25\2\177\u0080\5\65\33\2\u0080\u0081\5)\25\2\u0081"+
		"(\3\2\2\2\u0082\u0084\t\2\2\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2\2"+
		"\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086*\3\2\2\2\u0087\u008b\5"+
		"9\35\2\u0088\u008a\n\3\2\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b"+
		"\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2"+
		"\2\2\u008e\u008f\59\35\2\u008f,\3\2\2\2\u0090\u0091\7-\2\2\u0091.\3\2"+
		"\2\2\u0092\u0093\7/\2\2\u0093\60\3\2\2\2\u0094\u0095\7,\2\2\u0095\62\3"+
		"\2\2\2\u0096\u0097\7\61\2\2\u0097\64\3\2\2\2\u0098\u0099\7\60\2\2\u0099"+
		"\66\3\2\2\2\u009a\u009b\7#\2\2\u009b8\3\2\2\2\u009c\u009d\7$\2\2\u009d"+
		":\3\2\2\2\u009e\u00a2\t\4\2\2\u009f\u00a1\t\5\2\2\u00a0\u009f\3\2\2\2"+
		"\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3<\3"+
		"\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\t\6\2\2\u00a6\u00a5\3\2\2\2\u00a7"+
		"\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2"+
		"\2\2\u00aa\u00ab\b\37\2\2\u00ab>\3\2\2\2\7\2\u0085\u008b\u00a2\u00a8\3"+
		"\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}