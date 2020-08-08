#include <iostream>
#include <vector>
#include <cmath>
#include <deque>
#include <stack>
#include <unordered_map>
#include <algorithm>


char SPACE = 32;
char ZERO = 48;
char NINE = 57;
char DOT = 46;
char LEFT_PAREN = 40;
char RIGHT_PAREN = 41;
char MULTIPLICATION = 42;
char ADDITION = 43;
char SUBTRACTION = 45;
char DIVISION = 47;
char POWER = 94;
char MODULO = 37;

class Token {
private:
    std::string text;
public:
    explicit Token(std::string text);

    virtual std::string to_string() = 0;

    const std::string &get_text() const;
};

Token::Token(std::string text) : text(std::move(text)) {}

const std::string &Token::get_text() const {
    return text;
}


enum Associativity {
    LEFT,
    RIGHT
};

class Operator : public Token {
private:
    int precedence;
    Associativity associativity;
public:
    Operator(const std::string &text, int precedence, Associativity associativity);

    std::string to_string() override;

    virtual double evaluate(const std::vector<double> &numbers) = 0;

    int get_precedence() const;

    Associativity get_associativity() const;
};

class Addition : public Operator {
public:
    Addition(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Subtraction : public Operator {
public:
    Subtraction(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Multiplication : public Operator {
public:
    Multiplication(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Division : public Operator {
public:
    Division(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Modulo : public Operator {
public:
    Modulo(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Power : public Operator {
public:
    Power(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Minus : public Operator {
public:
    Minus(const std::string &text, int precedence, Associativity associativity);

    double evaluate(const std::vector<double> &numbers) override;
};

class Parenthesis : public Token {
private:
    Associativity associativity;
public:
    explicit Parenthesis(const std::string &text);

    std::string to_string() override;

    bool is_left();
};


Operator::Operator(const std::string &text, int precedence, Associativity associativity) : Token(text) {
    this->associativity = associativity;
    this->precedence = precedence;
}

Addition::Addition(const std::string &text, int precedence, Associativity associativity) : Operator(text, precedence,
                                                                                                    associativity) {}

Subtraction::Subtraction(const std::string &text, int precedence, Associativity associativity) : Operator(text,
                                                                                                          precedence,
                                                                                                          associativity) {}

Multiplication::Multiplication(const std::string &text, int precedence, Associativity associativity) : Operator(text,
                                                                                                                precedence,
                                                                                                                associativity) {}

Division::Division(const std::string &text, int precedence, Associativity associativity) : Operator(text, precedence,
                                                                                                    associativity) {}

Power::Power(const std::string &text, int precedence, Associativity associativity) : Operator(text, precedence,
                                                                                              associativity) {}

Minus::Minus(const std::string &text, int precedence, Associativity associativity) : Operator(text, precedence,
                                                                                              associativity) {}

Modulo::Modulo(const std::string &text, int precedence, Associativity associativity) : Operator(text, precedence,
                                                                                                associativity) {}


Parenthesis::Parenthesis(const std::string &text) : Token(text) {
    if (text == "(") {
        this->associativity = LEFT;
    } else {
        this->associativity = RIGHT;
    }
}

bool Parenthesis::is_left() {
    return associativity == LEFT;
}

std::string Parenthesis::to_string() {
    return (associativity == LEFT) ? "(" : ")";
}

std::string Operator::to_string() {
    return get_text();
}

int Operator::get_precedence() const {
    return precedence;
}

Associativity Operator::get_associativity() const {
    return associativity;
}

double Addition::evaluate(const std::vector<double> &numbers) {
    return numbers[0] + numbers[1];
}

double Subtraction::evaluate(const std::vector<double> &numbers) {
    return numbers[0] - numbers[1];
}

double Multiplication::evaluate(const std::vector<double> &numbers) {
    return numbers[0] * numbers[1];
}

double Division::evaluate(const std::vector<double> &numbers) {
    return numbers[0] / numbers[1];
}

double Power::evaluate(const std::vector<double> &numbers) {
    return pow(numbers[0], numbers[1]);
}

double Modulo::evaluate(const std::vector<double> &numbers) {
    return fmod(numbers[0], numbers[1]);
}

double Minus::evaluate(const std::vector<double> &numbers) {
    return -numbers[0];
}


class Number : public Token {
private:
    double value;
public:
    explicit Number(const std::string &text);

    explicit Number(double value);

    std::string to_string() override;

    double get_value() const;
};


Number::Number(const std::string &text) : Token(text) {
    this->value = std::stod(text);
}

std::string Number::to_string() {
    return std::to_string(value);
}

double Number::get_value() const {
    return value;
}

Number::Number(double value) : Token(std::to_string(value)) {
    this->value = value;
}


class ExpressionParser {
private:
    size_t index;
    std::string infix_expression;
    std::deque<Token *> output_queue;
    std::stack<Token *> tokens_stack;
    std::unordered_map<std::string, Token *> operators;
    std::unordered_map<std::string, Number *> memory;

public:
    explicit ExpressionParser(std::unordered_map<std::string, Token *> operators);

    Token *read_next_token();

public:

    void move_index_by_white_spaces();

    double evaluate_expression(const std::string &infix_expression);

    double evaluate_postfix_expression();

    void parse_expression_to_postfix();

    void preprocess_input_expression();

    static bool is_digit(char &sign);

    static bool is_operator(char &sign);

    static bool is_operator(Token *token);

    static Operator *to_operator(Token *token);

    static bool is_number(char &sign);

    static bool is_number(Token *token);

    static bool is_parenthesis(char &sign);

    static bool is_parenthesis(Token *token);

    static bool is_left_parenthesis(Token *token);

    static bool is_minus(Token *token);

    static Parenthesis *to_parenthesis(Token *token);

    Token *build_next_number_token();

    static bool is_dot(char sign);

    Token *build_next_operator_token();

    Token *build_next_parenthesis_token();

    bool is_greater_equal_precedence_on_stack(Token *token) const;

    bool is_left_parenthesis_on_stack() const;

    void pop_stack_to_output_queue();

    void print_postfix();

    void process_operator_token(Token *token);

    void process_parenthesis_token(Token *token);

    void move_stack_operators_to_output();

    static Number *to_number(Token *token);

    void process_token(Token *token);

    Token *build_next_variable_token();

    double interpret(std::string expression);

    static bool contains_sign(const std::string &expression, char sign);

    void ltrim(std::string &s);

    void rtrim(std::string &s);

    void trim(std::string &s);
};

ExpressionParser::ExpressionParser(std::unordered_map<std::string, Token *> operators) {
    this->index = 0;
    this->operators = std::move(operators);
}

Token *ExpressionParser::read_next_token() {
    Token *token = nullptr;
    move_index_by_white_spaces();

    if (is_digit(infix_expression[index])) {
        token = build_next_number_token();
    } else if (is_operator(infix_expression[index])) {
        token = build_next_operator_token();
    } else if (is_parenthesis(infix_expression[index])) {
        token = build_next_parenthesis_token();
    } else if (isalpha(infix_expression[index])) {
        token = build_next_variable_token();
    }

    return token;
}

void ExpressionParser::move_index_by_white_spaces() {
    while (index < infix_expression.length() && infix_expression[index] == ' ') {
        index++;
    }
}

bool ExpressionParser::is_digit(char &sign) {
    return sign >= ZERO && sign <= NINE;
}

bool ExpressionParser::is_operator(char &sign) {
    return sign == ADDITION || sign == SUBTRACTION || sign == MULTIPLICATION || sign == DIVISION || sign == POWER ||
           sign == MODULO;
}

bool ExpressionParser::is_parenthesis(char &sign) {
    return sign == LEFT_PAREN || sign == RIGHT_PAREN;
}

bool ExpressionParser::is_dot(char sign) {
    return sign == DOT;
}

bool ExpressionParser::is_number(char &sign) {
    return false;
}

bool ExpressionParser::is_number(Token *token) {
    return dynamic_cast<Number *>(token) != nullptr;
}

bool ExpressionParser::is_operator(Token *token) {
    return dynamic_cast<Operator *>(token) != nullptr;
}

Operator *ExpressionParser::to_operator(Token *token) {
    return dynamic_cast<Operator *>(token);
}

bool ExpressionParser::is_parenthesis(Token *token) {
    return dynamic_cast<Parenthesis *>(token) != nullptr;
}

Parenthesis *ExpressionParser::to_parenthesis(Token *token) {
    return dynamic_cast<Parenthesis *>(token);
}

Number *ExpressionParser::to_number(Token *token) {
    return dynamic_cast<Number *>(token);
}

bool ExpressionParser::is_minus(Token *token) {
    return dynamic_cast<Minus *>(token) != nullptr;
}

bool ExpressionParser::is_left_parenthesis(Token *token) {
    if (!is_parenthesis(token)) {
        return false;
    } else {
        return to_parenthesis(token)->is_left();
    }
}

Token *ExpressionParser::build_next_number_token() {
    size_t start_index = index;
    char sign = infix_expression[index];

    while (index < infix_expression.length() && is_digit(sign)) {
        index++;
        sign = infix_expression[index];
    }
    return new Number(infix_expression.substr(start_index, index - start_index));
}

Token *ExpressionParser::build_next_variable_token() {
    size_t start_index = index;
    char sign = infix_expression[index];

    while (index < infix_expression.length() && (isalnum(sign) || sign == '_')) {
        index++;
        sign = infix_expression[index];
    }
    std::string variable = infix_expression.substr(start_index, index - start_index);

    if(memory.find(variable) == memory.end()) {
        throw std::exception();
    }
    return new Number(memory.at(variable)->get_value());
}

Token *ExpressionParser::build_next_operator_token() {
    Operator *operation = nullptr;
    if (infix_expression[index] == SUBTRACTION && infix_expression[index + 1] != SPACE) {
        Token *token = operators.at("#");
        operation = to_operator(token);

    } else {
        operation = to_operator(operators.at(std::string(1, infix_expression[index])));
    }
    index++;
    return operation;
}

Token *ExpressionParser::build_next_parenthesis_token() {
    Token *token = operators.at(std::string(1, infix_expression[index]));
    index++;
    return token;
}

void ExpressionParser::parse_expression_to_postfix() {
    while (index < infix_expression.length()) {
        Token *token = read_next_token();
        if (is_minus(token)) {

            process_token(operators.at("("));
            process_token(new Number(-1));
            process_token(operators.at(")"));
            tokens_stack.push(operators.at("*"));
        } else {
            process_token(token);
        }
    }
    move_stack_operators_to_output();
}

void ExpressionParser::process_token(Token *token) {
    if (is_number(token)) {
        output_queue.push_back(token);
    } else if (is_operator(token)) {
        process_operator_token(token);
    } else if (is_parenthesis(token)) {
        process_parenthesis_token(token);
    }
}

void ExpressionParser::move_stack_operators_to_output() {
    while (!tokens_stack.empty()) {
        output_queue.push_back(tokens_stack.top());
        tokens_stack.pop();
    }
}

void ExpressionParser::process_parenthesis_token(Token *token) {
    if (is_left_parenthesis(token)) {
        tokens_stack.push(token);
    } else {
        while (!is_left_parenthesis_on_stack()) {
            pop_stack_to_output_queue();
        }
        if (is_left_parenthesis_on_stack()) {
            tokens_stack.pop();
        }
    }
}

void ExpressionParser::process_operator_token(Token *token) {
    while (!is_left_parenthesis_on_stack() && is_greater_equal_precedence_on_stack(token)) {
        pop_stack_to_output_queue();
    }
    tokens_stack.push(token);
}

void ExpressionParser::pop_stack_to_output_queue() {
    output_queue.push_back(tokens_stack.top());
    tokens_stack.pop();
}

bool ExpressionParser::is_left_parenthesis_on_stack() const {
    return !tokens_stack.empty() && is_left_parenthesis(tokens_stack.top());
}

bool ExpressionParser::is_greater_equal_precedence_on_stack(Token *token) const {
    return !tokens_stack.empty() && is_operator(tokens_stack.top()) && to_operator(
            tokens_stack.top())->get_precedence() >= to_operator(token)->get_precedence();
}

double ExpressionParser::evaluate_expression(const std::string &expression) {
    this->index = 0;
    this->infix_expression = expression;
    this->output_queue.clear();
    parse_expression_to_postfix();
//    std::cout << "\n" << std::endl;
//    print_postfix();
//    std::cout << "\n" << std::endl;
    return evaluate_postfix_expression();
}

double ExpressionParser::evaluate_postfix_expression() {
    std::stack<Token *> stack;

    for (auto const token: output_queue) {
        if (is_number(token)) {
            stack.push(token);
        } else {
            Number *number2 = to_number(stack.top());
            stack.pop();
            Number *number1 = to_number(stack.top());
            stack.pop();
            Operator *operation = to_operator(token);
            double result = operation->evaluate(std::vector<double>{number1->get_value(), number2->get_value()});
            delete number1;
            delete number2;

            stack.push(new Number(result));
        }
    }

    if (stack.size() == 2) {
        Number *number2 = to_number(stack.top());
        stack.pop();
        Number *number1 = to_number(stack.top());
        stack.pop();
        auto operation = to_operator(operators.at("+"));
        double result = operation->evaluate(std::vector<double>{number1->get_value(), number2->get_value()});
        return result;
    } else {
        Number *result = to_number(stack.top());
        double final_result = result->get_value();
        delete result;

        return final_result;
    }
}

void ExpressionParser::print_postfix() {
    for (auto const &token: output_queue) {
        std::cout << token->to_string() << " ";
    }
}

void ExpressionParser::preprocess_input_expression() {
    if (infix_expression[0] == SUBTRACTION) {

    }
}

double ExpressionParser::interpret(std::string expression) {

    if (contains_sign(expression, '=')) {
        size_t index = expression.find('=');

        std::string left = expression.substr(0, index);
        std::string right = expression.substr(index + 1, expression.length() - index);

        trim(left);
        trim(right);

        memory[left] = new Number(evaluate_expression(right));
        return memory[left]->get_value();
    } else {
        trim(expression);
        if(expression.length() == 0) {
            throw std::exception();
        }
        return (new Number(evaluate_expression(expression)))->get_value();
    }
    return 0;
}

bool ExpressionParser::contains_sign(const std::string &expression, char sign) {
    return expression.find(sign) != std::string::npos;
}

void ExpressionParser::trim(std::string &s) {
    ltrim(s);
    rtrim(s);
}

void ExpressionParser::rtrim(std::string &s) {
    s.erase(std::find_if(s.rbegin(), s.rend(), [](int ch) {
        return !std::isspace(ch);
    }).base(), s.end());
}

void ExpressionParser::ltrim(std::string &s) {
    s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](int ch) {
        return !std::isspace(ch);
    }));
}

Token *addition = new Addition("+", 2, Associativity(LEFT));
Token *subtraction = new Subtraction("-", 2, Associativity(LEFT));
Token *multiplication = new Multiplication("*", 3, Associativity(LEFT));
Token *division = new Division("/", 3, Associativity(LEFT));
Token *modulo = new Modulo("%", 3, Associativity(LEFT));
Token *left_paren = new Parenthesis("(");
Token *right_paren = new Parenthesis(")");
Token *minus = new Minus("#", 4, Associativity(RIGHT));

std::unordered_map<std::string, Token *> operators = {
        {"+", addition},
        {"-", subtraction},
        {"*", multiplication},
        {"/", division},
        {"%", modulo},
        {"#", minus},
        {"(", left_paren},
        {")", right_paren},
};


ExpressionParser parser(operators);

double interpret(std::string expression) {
    return parser.interpret(expression);
}

int main () {
    std::cout << interpret("(2 + 2 *        4)  % 4") << std::endl;
}