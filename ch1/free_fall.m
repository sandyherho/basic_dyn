clear; close all; clc

grv_const = 9.81; % [m/s]
init_post = 0; % [m]
init_vel = 0.5; % [m/s]
init_mass = 5; % [kg]

init_time = 0; % [s]
final_time = 5; % [s]
time_interval = [init_time final_time];

x0 = [init_post init_vel init_mass];

[tout, xout] = ode45(@(time, state) free_falling_obj(time, state, grv_const), ...
    time_interval, x0);

figure(1)
plot(tout, xout(:, 1))
ylabel('$x$ [m]', 'Interpreter','latex');
xlabel('$t$ [s]', 'Interpreter','latex');
grid on

figure(2)
plot(tout, xout(:, 2))
ylabel('$\dot{x}$ [m/s]', 'Interpreter','latex');
xlabel('$t$ [s]', 'Interpreter','latex');
grid on

figure(3)
plot(tout, xout(:, 3))
ylabel('$m$ [kg]', 'Interpreter','latex');
xlabel('$t$ [s]', 'Interpreter','latex');
grid on
