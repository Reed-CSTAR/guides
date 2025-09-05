# Services

We self-host some services that you can use.

## Coder

[Coder](https://coder.com) is a web app that provides access to development
environments running in Docker containers. This can be a convenient way to set
up an environment for some specialized tasks. It runs physically on Patty, so
it's got access to a good amount of compute. In particular, there's a
pre-existing template you can use to make a container for CUDA development if
you're having issues on your own machine or if you don't have an Nvidia GPU.

More detailed instructions on general use and configuring CUDA will be
available here soon. If you have a question or what some guidance right now,
send an email.

## Authentication

These services are all accessed via an SSO login *distinct from your normal
Reed credentials.* You can test your login (from a device on the Reed network)
by logging into [Polly](https://polly.reed.edu) over the web. Your username and
password for this SSO system is the same as that which you'd use to log in to
Polly over SSH.[^polly-pass]

[^polly-pass]: This isn't strictly true right now. If you change your password,
    you'll need to ping a CSTAR member (for now, Tali) to get everything to
    work. I (Tali) will make this automatic soon!
