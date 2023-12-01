#ArgsReqAndOptional.py
# show in debugger
def fn(p_req, p_opt = 1):
    print("p_req =", p_req, "and p_opt =", p_opt)

fn(3)                    # uses default value for p_opt
fn(2, 4)
fn(p_opt = 6)      # error ...the required argument is missing
