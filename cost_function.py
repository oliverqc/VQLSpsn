def cost_func(params, ansatz, H_op, H_op_norm, estimator, history):
    pub_numerator = (ansatz, H_op, params)
    pub_denominator = (ansatz, H_op_norm, params)

    job = estimator.run(pubs=[pub_numerator, pub_denominator])
    results = job.result()

    num_val = results[0].data.evs
    den_val = results[1].data.evs

    cost = num_val / den_val

    history.append(cost)
    print(f"  -> Iteration {len(history)}: Cost = {cost:.6f}")

    return cost
