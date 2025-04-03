# Smart Soles nTop Documentation

## Meshing via CLI


### ssh to the NURobotics computer
```
ssh robomember@<redacted IP> # Ask austin for IP / tailscale access
```

### start runner script to mesh
ssh to the NUrobotics computer
```
cd Documents\SmartSoles2\scripts
python runner.py
```

### Remove remote files
ssh to the NUrobotics computer
```
cd Documents\SmartSoles2\scripts
del runner.py # example, likely removing old input<x>.json files
```

### Editing runner script remotely
Make local changes, scp to remote machine

SCPs the nTop files, runner script, anything else needed
```
cd Documents/smart-soles-hw/ntop
scp -r scripts robomember@desktop-nurobotics.tailcd7641.ts.net:"C:/Users/robomember/Documents/SmartSoles2/"
```