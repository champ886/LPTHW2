def start_formula(started):
    jelly_beans = started * 6
    jars = jelly_beans/200
    crates = jars/ 50
    orders = jelly_beans * crates
    return jelly_beans, jars, crates, orders


start_point = 500
beans, jar_stuff, crate_things, client_orders = start_formula(start_point)


(start_formula(start_point))

print(f"beans =", beans)
print(f"jar_stuff =", jar_stuff)
print(f"crate_things =", crate_things)
print(f"client_orders =", client_orders)