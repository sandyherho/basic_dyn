function dxdt = free_falling_obj(time, state, grv_const)
    x1 = state(1);
    x2 = state(2);
    x3 = state(3);

    dxdt = zeros(3, 1);
    dxdt(1) = x2;
    dxdt(2) = grv_const + (x3 - 2) * (x2/x3);
    dxdt(3) = -x3 + 2;
end