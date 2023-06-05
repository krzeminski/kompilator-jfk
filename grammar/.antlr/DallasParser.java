// Generated from c:\Users\Admin\Desktop\Nowy folder\kompilator-jfk\grammar\Dallas.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DallasParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PRINT=1, READ=2, AND=3, OR=4, XOR=5, EQ=6, ASSIGN=7, COMMA=8, SEMI=9, 
		LPAREN=10, RPAREN=11, LCURLY=12, RCURLY=13, LBRACK=14, RBRACK=15, INT_KEY=16, 
		FLOAT_KEY=17, FLOAT_32_KEY=18, FLOAT_64_KEY=19, STRING_KEY=20, ARRAY_KEY=21, 
		FLOAT=22, INT=23, STRING=24, PLUS=25, MINUS=26, ASTERISK=27, SLASH=28, 
		DOT=29, EXCLAMATION=30, DQ=31, ID=32, WS=33;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_variableDeclaration = 2, RULE_printCall = 3, 
		RULE_readCall = 4, RULE_functionCall = 5, RULE_functionCallOnObject = 6, 
		RULE_functionCallOnString = 7, RULE_array = 8, RULE_assignment = 9, RULE_expression = 10, 
		RULE_additiveExpression = 11, RULE_multiplicativeExpression = 12, RULE_unaryExpression = 13, 
		RULE_primaryExpression = 14, RULE_dataType = 15, RULE_mathOperator = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "variableDeclaration", "printCall", "readCall", 
			"functionCall", "functionCallOnObject", "functionCallOnString", "array", 
			"assignment", "expression", "additiveExpression", "multiplicativeExpression", 
			"unaryExpression", "primaryExpression", "dataType", "mathOperator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "'read'", "'&&'", "'||'", "'^^'", "'=='", "'='", "','", 
			"';'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'int'", "'float'", 
			"'float32'", "'float64'", "'string'", "'array'", null, null, null, "'+'", 
			"'-'", "'*'", "'/'", "'.'", "'!'", "'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PRINT", "READ", "AND", "OR", "XOR", "EQ", "ASSIGN", "COMMA", "SEMI", 
			"LPAREN", "RPAREN", "LCURLY", "RCURLY", "LBRACK", "RBRACK", "INT_KEY", 
			"FLOAT_KEY", "FLOAT_32_KEY", "FLOAT_64_KEY", "STRING_KEY", "ARRAY_KEY", 
			"FLOAT", "INT", "STRING", "PLUS", "MINUS", "ASTERISK", "SLASH", "DOT", 
			"EXCLAMATION", "DQ", "ID", "WS"
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

	@Override
	public String getGrammarFileName() { return "Dallas.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DallasParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(DallasParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(34);
				statement();
				}
				}
				setState(37); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << READ) | (1L << LPAREN) | (1L << LBRACK) | (1L << INT_KEY) | (1L << FLOAT_KEY) | (1L << FLOAT_32_KEY) | (1L << FLOAT_64_KEY) | (1L << STRING_KEY) | (1L << ARRAY_KEY) | (1L << FLOAT) | (1L << INT) | (1L << STRING) | (1L << PLUS) | (1L << MINUS) | (1L << EXCLAMATION) | (1L << ID))) != 0) );
			setState(39);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public PrintCallContext printCall() {
			return getRuleContext(PrintCallContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(DallasParser.SEMI, 0); }
		public ReadCallContext readCall() {
			return getRuleContext(ReadCallContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallOnObjectContext functionCallOnObject() {
			return getRuleContext(FunctionCallOnObjectContext.class,0);
		}
		public FunctionCallOnStringContext functionCallOnString() {
			return getRuleContext(FunctionCallOnStringContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(41);
				variableDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(42);
				printCall();
				setState(43);
				match(SEMI);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(45);
				readCall();
				setState(46);
				match(SEMI);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(48);
				functionCall();
				setState(49);
				match(SEMI);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(51);
				functionCallOnObject();
				setState(52);
				match(SEMI);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(54);
				functionCallOnString();
				setState(55);
				match(SEMI);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(57);
				assignment();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(58);
				expression(0);
				setState(59);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclarationContext extends ParserRuleContext {
		public DataTypeContext dataType() {
			return getRuleContext(DataTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DallasParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(DallasParser.SEMI, 0); }
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variableDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			dataType();
			setState(64);
			match(ID);
			setState(65);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrintCallContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(DallasParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(DallasParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(DallasParser.RPAREN, 0); }
		public PrintCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printCall; }
	}

	public final PrintCallContext printCall() throws RecognitionException {
		PrintCallContext _localctx = new PrintCallContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_printCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(PRINT);
			setState(68);
			match(LPAREN);
			setState(69);
			expression(0);
			setState(70);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReadCallContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(DallasParser.READ, 0); }
		public TerminalNode LPAREN() { return getToken(DallasParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(DallasParser.RPAREN, 0); }
		public ReadCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_readCall; }
	}

	public final ReadCallContext readCall() throws RecognitionException {
		ReadCallContext _localctx = new ReadCallContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_readCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(READ);
			setState(73);
			match(LPAREN);
			setState(74);
			expression(0);
			setState(75);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DallasParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(DallasParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(DallasParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DallasParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DallasParser.COMMA, i);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(ID);
			setState(78);
			match(LPAREN);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LPAREN) | (1L << LBRACK) | (1L << FLOAT) | (1L << INT) | (1L << STRING) | (1L << PLUS) | (1L << MINUS) | (1L << EXCLAMATION) | (1L << ID))) != 0)) {
				{
				setState(79);
				expression(0);
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(80);
					match(COMMA);
					setState(81);
					expression(0);
					}
					}
					setState(86);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(89);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionCallOnObjectContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DallasParser.ID, 0); }
		public TerminalNode DOT() { return getToken(DallasParser.DOT, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallOnObjectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOnObject; }
	}

	public final FunctionCallOnObjectContext functionCallOnObject() throws RecognitionException {
		FunctionCallOnObjectContext _localctx = new FunctionCallOnObjectContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_functionCallOnObject);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(ID);
			setState(92);
			match(DOT);
			setState(93);
			functionCall();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionCallOnStringContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DallasParser.STRING, 0); }
		public TerminalNode DOT() { return getToken(DallasParser.DOT, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public FunctionCallOnStringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOnString; }
	}

	public final FunctionCallOnStringContext functionCallOnString() throws RecognitionException {
		FunctionCallOnStringContext _localctx = new FunctionCallOnStringContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_functionCallOnString);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(STRING);
			setState(96);
			match(DOT);
			setState(97);
			functionCall();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(DallasParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(DallasParser.RBRACK, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DallasParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DallasParser.COMMA, i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(LBRACK);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LPAREN) | (1L << LBRACK) | (1L << FLOAT) | (1L << INT) | (1L << STRING) | (1L << PLUS) | (1L << MINUS) | (1L << EXCLAMATION) | (1L << ID))) != 0)) {
				{
				setState(100);
				expression(0);
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(101);
					match(COMMA);
					setState(102);
					expression(0);
					}
					}
					setState(107);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(110);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DallasParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(DallasParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(DallasParser.SEMI, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(ID);
			setState(113);
			match(ASSIGN);
			setState(114);
			expression(0);
			setState(115);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DallasParser.ID, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode EXCLAMATION() { return getToken(DallasParser.EXCLAMATION, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AdditiveExpressionContext additiveExpression() {
			return getRuleContext(AdditiveExpressionContext.class,0);
		}
		public TerminalNode INT() { return getToken(DallasParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(DallasParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(DallasParser.STRING, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public TerminalNode OR() { return getToken(DallasParser.OR, 0); }
		public TerminalNode XOR() { return getToken(DallasParser.XOR, 0); }
		public TerminalNode AND() { return getToken(DallasParser.AND, 0); }
		public TerminalNode EQ() { return getToken(DallasParser.EQ, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(118);
				match(ID);
				}
				break;
			case 2:
				{
				setState(119);
				assignment();
				}
				break;
			case 3:
				{
				setState(120);
				functionCall();
				}
				break;
			case 4:
				{
				setState(121);
				match(EXCLAMATION);
				setState(122);
				expression(6);
				}
				break;
			case 5:
				{
				setState(123);
				additiveExpression(0);
				}
				break;
			case 6:
				{
				setState(124);
				match(INT);
				}
				break;
			case 7:
				{
				setState(125);
				match(FLOAT);
				}
				break;
			case 8:
				{
				setState(126);
				match(STRING);
				}
				break;
			case 9:
				{
				setState(127);
				array();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(144);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(142);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(130);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(131);
						match(OR);
						setState(132);
						expression(11);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(133);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(134);
						match(XOR);
						setState(135);
						expression(10);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(136);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(137);
						match(AND);
						setState(138);
						expression(9);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(139);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(140);
						match(EQ);
						setState(141);
						expression(8);
						}
						break;
					}
					} 
				}
				setState(146);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AdditiveExpressionContext extends ParserRuleContext {
		public MultiplicativeExpressionContext multiplicativeExpression() {
			return getRuleContext(MultiplicativeExpressionContext.class,0);
		}
		public AdditiveExpressionContext additiveExpression() {
			return getRuleContext(AdditiveExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(DallasParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(DallasParser.MINUS, 0); }
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		return additiveExpression(0);
	}

	private AdditiveExpressionContext additiveExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, _parentState);
		AdditiveExpressionContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_additiveExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(148);
			multiplicativeExpression(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(158);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(156);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						_localctx = new AdditiveExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_additiveExpression);
						setState(150);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(151);
						match(PLUS);
						setState(152);
						multiplicativeExpression(0);
						}
						break;
					case 2:
						{
						_localctx = new AdditiveExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_additiveExpression);
						setState(153);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(154);
						match(MINUS);
						setState(155);
						multiplicativeExpression(0);
						}
						break;
					}
					} 
				}
				setState(160);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public MultiplicativeExpressionContext multiplicativeExpression() {
			return getRuleContext(MultiplicativeExpressionContext.class,0);
		}
		public TerminalNode ASTERISK() { return getToken(DallasParser.ASTERISK, 0); }
		public TerminalNode SLASH() { return getToken(DallasParser.SLASH, 0); }
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		return multiplicativeExpression(0);
	}

	private MultiplicativeExpressionContext multiplicativeExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, _parentState);
		MultiplicativeExpressionContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_multiplicativeExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(162);
			unaryExpression();
			}
			_ctx.stop = _input.LT(-1);
			setState(172);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(170);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new MultiplicativeExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_multiplicativeExpression);
						setState(164);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(165);
						match(ASTERISK);
						setState(166);
						unaryExpression();
						}
						break;
					case 2:
						{
						_localctx = new MultiplicativeExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_multiplicativeExpression);
						setState(167);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(168);
						match(SLASH);
						setState(169);
						unaryExpression();
						}
						break;
					}
					} 
				}
				setState(174);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class UnaryExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(DallasParser.PLUS, 0); }
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(DallasParser.MINUS, 0); }
		public UnaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpression; }
	}

	public final UnaryExpressionContext unaryExpression() throws RecognitionException {
		UnaryExpressionContext _localctx = new UnaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_unaryExpression);
		try {
			setState(180);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
			case FLOAT:
			case INT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(175);
				primaryExpression();
				}
				break;
			case PLUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(176);
				match(PLUS);
				setState(177);
				unaryExpression();
				}
				break;
			case MINUS:
				enterOuterAlt(_localctx, 3);
				{
				setState(178);
				match(MINUS);
				setState(179);
				unaryExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryExpressionContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(DallasParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(DallasParser.FLOAT, 0); }
		public TerminalNode LPAREN() { return getToken(DallasParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(DallasParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(DallasParser.ID, 0); }
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_primaryExpression);
		try {
			setState(189);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(182);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				match(FLOAT);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 3);
				{
				setState(184);
				match(LPAREN);
				setState(185);
				expression(0);
				setState(186);
				match(RPAREN);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(188);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DataTypeContext extends ParserRuleContext {
		public TerminalNode INT_KEY() { return getToken(DallasParser.INT_KEY, 0); }
		public TerminalNode FLOAT_KEY() { return getToken(DallasParser.FLOAT_KEY, 0); }
		public TerminalNode FLOAT_32_KEY() { return getToken(DallasParser.FLOAT_32_KEY, 0); }
		public TerminalNode FLOAT_64_KEY() { return getToken(DallasParser.FLOAT_64_KEY, 0); }
		public TerminalNode STRING_KEY() { return getToken(DallasParser.STRING_KEY, 0); }
		public TerminalNode ARRAY_KEY() { return getToken(DallasParser.ARRAY_KEY, 0); }
		public DataTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dataType; }
	}

	public final DataTypeContext dataType() throws RecognitionException {
		DataTypeContext _localctx = new DataTypeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_dataType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_KEY) | (1L << FLOAT_KEY) | (1L << FLOAT_32_KEY) | (1L << FLOAT_64_KEY) | (1L << STRING_KEY) | (1L << ARRAY_KEY))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MathOperatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(DallasParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(DallasParser.MINUS, 0); }
		public TerminalNode ASTERISK() { return getToken(DallasParser.ASTERISK, 0); }
		public TerminalNode SLASH() { return getToken(DallasParser.SLASH, 0); }
		public MathOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mathOperator; }
	}

	public final MathOperatorContext mathOperator() throws RecognitionException {
		MathOperatorContext _localctx = new MathOperatorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_mathOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << ASTERISK) | (1L << SLASH))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 11:
			return additiveExpression_sempred((AdditiveExpressionContext)_localctx, predIndex);
		case 12:
			return multiplicativeExpression_sempred((MultiplicativeExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		}
		return true;
	}
	private boolean additiveExpression_sempred(AdditiveExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean multiplicativeExpression_sempred(MultiplicativeExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6:
			return precpred(_ctx, 2);
		case 7:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3#\u00c6\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\6\2&\n\2\r\2\16\2\'\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3@\n\3\3\4\3\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7U\n\7\f"+
		"\7\16\7X\13\7\5\7Z\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n"+
		"\3\n\3\n\7\nj\n\n\f\n\16\nm\13\n\5\no\n\n\3\n\3\n\3\13\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0083\n\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0091\n\f\f\f\16\f\u0094"+
		"\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u009f\n\r\f\r\16\r\u00a2"+
		"\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00ad\n\16\f\16"+
		"\16\16\u00b0\13\16\3\17\3\17\3\17\3\17\3\17\5\17\u00b7\n\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\5\20\u00c0\n\20\3\21\3\21\3\22\3\22\3\22\2\5"+
		"\26\30\32\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"\2\4\3\2\22\27\3"+
		"\2\33\36\2\u00d5\2%\3\2\2\2\4?\3\2\2\2\6A\3\2\2\2\bE\3\2\2\2\nJ\3\2\2"+
		"\2\fO\3\2\2\2\16]\3\2\2\2\20a\3\2\2\2\22e\3\2\2\2\24r\3\2\2\2\26\u0082"+
		"\3\2\2\2\30\u0095\3\2\2\2\32\u00a3\3\2\2\2\34\u00b6\3\2\2\2\36\u00bf\3"+
		"\2\2\2 \u00c1\3\2\2\2\"\u00c3\3\2\2\2$&\5\4\3\2%$\3\2\2\2&\'\3\2\2\2\'"+
		"%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\2\2\3*\3\3\2\2\2+@\5\6\4\2,-\5\b\5"+
		"\2-.\7\13\2\2.@\3\2\2\2/\60\5\n\6\2\60\61\7\13\2\2\61@\3\2\2\2\62\63\5"+
		"\f\7\2\63\64\7\13\2\2\64@\3\2\2\2\65\66\5\16\b\2\66\67\7\13\2\2\67@\3"+
		"\2\2\289\5\20\t\29:\7\13\2\2:@\3\2\2\2;@\5\24\13\2<=\5\26\f\2=>\7\13\2"+
		"\2>@\3\2\2\2?+\3\2\2\2?,\3\2\2\2?/\3\2\2\2?\62\3\2\2\2?\65\3\2\2\2?8\3"+
		"\2\2\2?;\3\2\2\2?<\3\2\2\2@\5\3\2\2\2AB\5 \21\2BC\7\"\2\2CD\7\13\2\2D"+
		"\7\3\2\2\2EF\7\3\2\2FG\7\f\2\2GH\5\26\f\2HI\7\r\2\2I\t\3\2\2\2JK\7\4\2"+
		"\2KL\7\f\2\2LM\5\26\f\2MN\7\r\2\2N\13\3\2\2\2OP\7\"\2\2PY\7\f\2\2QV\5"+
		"\26\f\2RS\7\n\2\2SU\5\26\f\2TR\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W"+
		"Z\3\2\2\2XV\3\2\2\2YQ\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\r\2\2\\\r\3\2\2"+
		"\2]^\7\"\2\2^_\7\37\2\2_`\5\f\7\2`\17\3\2\2\2ab\7\32\2\2bc\7\37\2\2cd"+
		"\5\f\7\2d\21\3\2\2\2en\7\20\2\2fk\5\26\f\2gh\7\n\2\2hj\5\26\f\2ig\3\2"+
		"\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2lo\3\2\2\2mk\3\2\2\2nf\3\2\2\2no\3\2"+
		"\2\2op\3\2\2\2pq\7\21\2\2q\23\3\2\2\2rs\7\"\2\2st\7\t\2\2tu\5\26\f\2u"+
		"v\7\13\2\2v\25\3\2\2\2wx\b\f\1\2x\u0083\7\"\2\2y\u0083\5\24\13\2z\u0083"+
		"\5\f\7\2{|\7 \2\2|\u0083\5\26\f\b}\u0083\5\30\r\2~\u0083\7\31\2\2\177"+
		"\u0083\7\30\2\2\u0080\u0083\7\32\2\2\u0081\u0083\5\22\n\2\u0082w\3\2\2"+
		"\2\u0082y\3\2\2\2\u0082z\3\2\2\2\u0082{\3\2\2\2\u0082}\3\2\2\2\u0082~"+
		"\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083"+
		"\u0092\3\2\2\2\u0084\u0085\f\f\2\2\u0085\u0086\7\6\2\2\u0086\u0091\5\26"+
		"\f\r\u0087\u0088\f\13\2\2\u0088\u0089\7\7\2\2\u0089\u0091\5\26\f\f\u008a"+
		"\u008b\f\n\2\2\u008b\u008c\7\5\2\2\u008c\u0091\5\26\f\13\u008d\u008e\f"+
		"\t\2\2\u008e\u008f\7\b\2\2\u008f\u0091\5\26\f\n\u0090\u0084\3\2\2\2\u0090"+
		"\u0087\3\2\2\2\u0090\u008a\3\2\2\2\u0090\u008d\3\2\2\2\u0091\u0094\3\2"+
		"\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\27\3\2\2\2\u0094\u0092"+
		"\3\2\2\2\u0095\u0096\b\r\1\2\u0096\u0097\5\32\16\2\u0097\u00a0\3\2\2\2"+
		"\u0098\u0099\f\4\2\2\u0099\u009a\7\33\2\2\u009a\u009f\5\32\16\2\u009b"+
		"\u009c\f\3\2\2\u009c\u009d\7\34\2\2\u009d\u009f\5\32\16\2\u009e\u0098"+
		"\3\2\2\2\u009e\u009b\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0"+
		"\u00a1\3\2\2\2\u00a1\31\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\b\16\1"+
		"\2\u00a4\u00a5\5\34\17\2\u00a5\u00ae\3\2\2\2\u00a6\u00a7\f\4\2\2\u00a7"+
		"\u00a8\7\35\2\2\u00a8\u00ad\5\34\17\2\u00a9\u00aa\f\3\2\2\u00aa\u00ab"+
		"\7\36\2\2\u00ab\u00ad\5\34\17\2\u00ac\u00a6\3\2\2\2\u00ac\u00a9\3\2\2"+
		"\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\33"+
		"\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b7\5\36\20\2\u00b2\u00b3\7\33\2"+
		"\2\u00b3\u00b7\5\34\17\2\u00b4\u00b5\7\34\2\2\u00b5\u00b7\5\34\17\2\u00b6"+
		"\u00b1\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\35\3\2\2"+
		"\2\u00b8\u00c0\7\31\2\2\u00b9\u00c0\7\30\2\2\u00ba\u00bb\7\f\2\2\u00bb"+
		"\u00bc\5\26\f\2\u00bc\u00bd\7\r\2\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\7"+
		"\"\2\2\u00bf\u00b8\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00ba\3\2\2\2\u00bf"+
		"\u00be\3\2\2\2\u00c0\37\3\2\2\2\u00c1\u00c2\t\2\2\2\u00c2!\3\2\2\2\u00c3"+
		"\u00c4\t\3\2\2\u00c4#\3\2\2\2\21\'?VYkn\u0082\u0090\u0092\u009e\u00a0"+
		"\u00ac\u00ae\u00b6\u00bf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}