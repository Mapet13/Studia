struct Stack;
typedef DataType;

void init_stack(struct Stack*);
struct Stack* create_stack(void);
void destroy_stack(struct Stack*);
void push(struct Stack*, DataType);
DataType pop(struct Stack*);
int is_empty(struct Stack*);