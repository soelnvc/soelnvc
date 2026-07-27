import os

def generate_svg(mode):
    is_dark = mode == 'dark'
    
    # Colors
    bg_color = "#030712" if is_dark else "#FFFFFF"
    panel_color = "#0F172A" if is_dark else "#F8FAFC"
    border_color = "rgba(255,255,255,0.08)" if is_dark else "rgba(15,23,42,0.08)"
    text_primary = "#F8FAFC" if is_dark else "#0F172A"
    text_muted = "#94A3B8" if is_dark else "#475569"
    
    accent_start = "#7C3AED" if is_dark else "#2563EB"
    accent_mid = "#22D3EE" if is_dark else "#06B6D4"
    accent_end = "#10B981" if is_dark else "#10B981"
    
    ascii_grad_start = "#06b6d4" if is_dark else "#3b82f6"
    ascii_grad_end = "#a855f7" if is_dark else "#06b6d4"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610">
    <defs>
        <!-- Gradients -->
        <linearGradient id="bgGlow" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{accent_start}" stop-opacity="0.15">
                <animate attributeName="stop-color" values="{accent_start};{accent_mid};{accent_end};{accent_start}" dur="10s" repeatCount="indefinite" />
            </stop>
            <stop offset="50%" stop-color="{accent_mid}" stop-opacity="0.05">
                <animate attributeName="stop-color" values="{accent_mid};{accent_end};{accent_start};{accent_mid}" dur="10s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{accent_end}" stop-opacity="0.15">
                <animate attributeName="stop-color" values="{accent_end};{accent_start};{accent_mid};{accent_end}" dur="10s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{ascii_grad_start}">
                <animate attributeName="stop-color" values="{ascii_grad_start};{ascii_grad_end};{ascii_grad_start}" dur="5s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{ascii_grad_end}">
                <animate attributeName="stop-color" values="{ascii_grad_end};{ascii_grad_start};{ascii_grad_end}" dur="5s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{accent_start}" />
            <stop offset="50%" stop-color="{accent_mid}" />
            <stop offset="100%" stop-color="{accent_end}" />
            <animate attributeName="x1" values="0%;100%;0%" dur="8s" repeatCount="indefinite" />
            <animate attributeName="x2" values="100%;200%;100%" dur="8s" repeatCount="indefinite" />
        </linearGradient>
        
        <radialGradient id="glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{accent_mid}" stop-opacity="0.3" />
            <stop offset="100%" stop-color="{accent_mid}" stop-opacity="0" />
        </radialGradient>
        
        <!-- Filters -->
        <filter id="glass" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="10" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        
        <filter id="neon" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1" />
            <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur2" />
            <feMerge>
                <feMergeNode in="blur2" />
                <feMergeNode in="blur1" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        
        <!-- Clip Paths -->
        <clipPath id="terminalClip">
            <rect x="0" y="0" width="700" height="550" rx="12" />
        </clipPath>
        
        <clipPath id="asciiClip">
            <rect x="0" y="0" width="410" height="550" rx="12" />
        </clipPath>
    </defs>

    <!-- Background -->
    <rect width="1180" height="610" fill="{bg_color}" rx="16" />
    <rect width="1180" height="610" fill="url(#bgGlow)" rx="16" />
    
    <!-- Particles -->
    <g opacity="0.4">
"""
    
    import random
    random.seed(42)
    for i in range(20):
        x = random.randint(0, 1180)
        y = random.randint(0, 610)
        r = random.uniform(1, 3)
        dur = random.uniform(5, 10)
        delay = random.uniform(0, 5)
        svg += f'        <circle cx="{x}" cy="{y}" r="{r}" fill="{accent_mid}">\n'
        svg += f'            <animate attributeName="cy" values="{y};{y-100};{y}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />\n'
        svg += f'            <animate attributeName="opacity" values="0;1;0" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />\n'
        svg += '        </circle>\n'
        
    svg += f"""    </g>

    <!-- Left Side: ASCII Portrait (approx 38% = 450px) -->
    <g transform="translate(30, 30)">
        <rect width="410" height="550" fill="{panel_color}" fill-opacity="0.7" rx="12" stroke="{border_color}" stroke-width="1" />
        
        <!-- ASCII Floating animation -->
        <g clip-path="url(#asciiClip)">
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-10; 0,0" dur="6s" repeatCount="indefinite" />
            
            <text x="20" y="40" font-family="monospace" font-size="8" fill="url(#asciiGrad)" style="white-space: pre;">
"""
    
    # Generate some cool ASCII art
    ascii_art = [
        "                 .::::.                 ",
        "               .::::::::.               ",
        "              ::::::::::::              ",
        "             ..::::::::::..             ",
        "            . '::::::::::' .            ",
        "           .   '::::::::'   .           ",
        "          .      '::::'      .          ",
        "         .       .::::.       .         ",
        "        .      .::::::::.      .        ",
        "       .      ::::::::::::      .       ",
        "      .     ..::::::::::::..     .      ",
        "     .     . '::::::::::::' .     .     ",
        "    .     .   '::::::::::'   .     .    ",
        "   .     .      '::::::'      .     .   ",
        "  .     .       .::::::.       .     .  ",
        " .     .      .::::::::::.      .     . ",
        "      .      ::::::::::::::      .      ",
        "     .     ..::::::::::::::..     .     ",
        "    .     . '::::::::::::::' .     .    ",
        "   .     .   '::::::::::::'   .     .   ",
        "  .     .      '::::::::'      .     .  ",
        " .     .       .::::::::.       .     . ",
        "      .      .::::::::::::.      .      ",
        "     .      ::::::::::::::::      .     ",
        "    .     ..::::::::::::::::..     .    ",
        "   .     . '::::::::::::::::' .     .   ",
        "  .     .   '::::::::::::::'   .     .  ",
        " .     .      '::::::::::'      .     . ",
        "      .       .::::::::::.       .      ",
        "     .      .::::::::::::::.      .     ",
        "    .      ::::::::::::::::::      .    ",
        "   .     ..::::::::::::::::::..     .   ",
        "  .     . '::::::::::::::::::' .     .  ",
        " .     .   '::::::::::::::::'   .     . ",
        "      .      '::::::::::::'      .      ",
        "     .       .::::::::::::.       .     ",
        "    .      .::::::::::::::::.      .    ",
        "   .      ::::::::::::::::::::      .   ",
        "  .     ..::::::::::::::::::::..     .  ",
        " .     . '::::::::::::::::::::' .     . ",
    ]
    
    for i, line in enumerate(ascii_art):
        svg += f'                <tspan x="20" dy="12" opacity="0">\n'
        svg += f'                    {line}\n'
        svg += f'                    <animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" dur="10s" begin="{i*0.05}s" fill="freeze" />\n'
        svg += f'                </tspan>\n'
        
    svg += f"""            </text>
            
            <!-- Scanline effect -->
            <rect x="0" y="0" width="410" height="4" fill="{accent_mid}" opacity="0.3">
                <animate attributeName="y" values="0;550;0" dur="4s" repeatCount="indefinite" />
            </rect>
        </g>
    </g>

    <!-- Right Side: Terminal (approx 62% = 730px) -->
    <g transform="translate(460, 30)">
        <rect width="690" height="550" fill="{panel_color}" fill-opacity="0.8" rx="12" stroke="{border_color}" stroke-width="1" />
        
        <!-- Terminal Header -->
        <path d="M 0 12 Q 0 0 12 0 L 678 0 Q 690 0 690 12 L 690 40 L 0 40 Z" fill="{bg_color}" fill-opacity="0.5" />
        <circle cx="20" cy="20" r="6" fill="#EF4444" />
        <circle cx="40" cy="20" r="6" fill="#F59E0B" />
        <circle cx="60" cy="20" r="6" fill="#10B981" />
        <text x="345" y="25" font-family="monospace" font-size="12" fill="{text_muted}" text-anchor="middle">visitor@portfolio:~</text>
        
        <!-- Terminal Body -->
        <g transform="translate(30, 80)" font-family="monospace" font-size="16">
            
            <!-- Greeting -->
            <text x="0" y="0" fill="{text_primary}" font-weight="bold" font-size="24">
                Hi 👋 I'm <tspan fill="url(#accentGrad)">{{NAME}}</tspan>
            </text>

            <!-- Animated Typing Text Roles -->
            <g transform="translate(0, 40)">
                <text x="0" y="0" fill="{text_primary}">
                    <tspan>> </tspan>
                </text>
                
"""
    
    roles = ["Frontend Engineer", "Full Stack Developer", "Open Source Contributor", "UI Engineer", "AI Enthusiast"]
    for i, role in enumerate(roles):
        begin_time = i * 4
        svg += f'                <g opacity="0">\n'
        svg += f'                    <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.05;0.8;0.85;1" dur="{len(roles)*4}s" begin="{begin_time}s" repeatCount="indefinite" />\n'
        
        svg += f'                    <clipPath id="clipRole{i}">\n'
        svg += f'                        <rect x="20" y="-15" width="0" height="20">\n'
        svg += f'                            <animate attributeName="width" values="0;300;300" keyTimes="0;0.3;1" dur="4s" begin="{begin_time}s" repeatCount="indefinite" />\n'
        svg += f'                        </rect>\n'
        svg += f'                    </clipPath>\n'
        
        svg += f'                    <text x="20" y="0" fill="{text_primary}" clip-path="url(#clipRole{i})">{role}</text>\n'
        svg += f'                </g>\n'

    svg += f"""
                <!-- Blinking Cursor -->
                <text x="20" y="0" fill="{accent_mid}">
                    <tspan>_</tspan>
                    <animateTransform attributeName="transform" type="translate" values="0,0; 200,0; 200,0; 0,0" keyTimes="0; 0.3; 0.8; 1" dur="4s" repeatCount="indefinite" />
                    <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
                </text>
            </g>
            
            <!-- Sequential Reveal Info -->
            <g transform="translate(0, 100)" font-size="15">
"""

    info = [
        ("Location", "San Francisco, CA"),
        ("Education", "B.S. Computer Science"),
        ("Current Focus", "Building Next-Gen UIs"),
        ("Portfolio", "portfolio.dev"),
        ("Email", "hello@portfolio.dev")
    ]
    
    for i, (key, val) in enumerate(info):
        svg += f'                <g opacity="0">\n'
        svg += f'                    <animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" dur="100s" begin="{2 + i*0.5}s" fill="freeze" />\n'
        svg += f'                    <text x="0" y="{i*30}">\n'
        svg += f'                        <tspan fill="{text_muted}" font-weight="bold">{key.ljust(15)}</tspan>\n'
        svg += f'                        <tspan fill="{accent_mid}">...</tspan>\n'
        svg += f'                        <tspan fill="{text_primary}"> {val}</tspan>\n'
        svg += f'                    </text>\n'
        svg += f'                </g>\n'

    svg += f"""            </g>
            
            <!-- Skills Section -->
            <g transform="translate(0, 280)">
                <text x="0" y="0" fill="{text_muted}" font-weight="bold">Core Skills:</text>
                <g transform="translate(0, 20)">
"""
    
    skills = ["React", "Next.js", "Node.js", "TypeScript", "Tailwind", "Python", "Docker", "Postgres", "AWS", "Git", "Figma"]
    
    x_pos = 0
    y_pos = 0
    for i, skill in enumerate(skills):
        skill_width = len(skill) * 10 + 30
        if x_pos + skill_width > 600:
            x_pos = 0
            y_pos += 40
            
        svg += f'                    <g transform="translate({x_pos}, {y_pos})" opacity="0" id="pill-{i}">\n'
        svg += f'                        <animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" dur="100s" begin="{4.5 + i*0.2}s" fill="freeze" />\n'
        svg += f'                        <rect id="rect-{i}" x="0" y="0" width="{skill_width}" height="28" rx="14" fill="{panel_color}" stroke="{border_color}" stroke-width="1">\n'
        svg += f'                            <animate attributeName="stroke" values="{border_color};{accent_mid};{border_color}" begin="pill-{i}.mouseover" end="pill-{i}.mouseout" dur="0.3s" fill="freeze" />\n'
        svg += f'                            <animate attributeName="fill" values="{panel_color};{bg_color};{panel_color}" begin="pill-{i}.mouseover" end="pill-{i}.mouseout" dur="0.3s" fill="freeze" />\n'
        svg += f'                        </rect>\n'
        svg += f'                        <text x="{skill_width/2}" y="19" fill="{text_primary}" text-anchor="middle" font-size="13">{skill}</text>\n'
        svg += f'                        <animateTransform attributeName="transform" type="scale" values="1;1.05;1" begin="pill-{i}.mouseover" end="pill-{i}.mouseout" dur="0.3s" fill="freeze" additive="sum" />\n'
        svg += f'                    </g>\n'
        
        x_pos += skill_width + 15

    svg += f"""                </g>
            </g>
            
            <!-- Social Icons -->
            <g transform="translate(0, 420)">
                <rect x="0" y="0" width="630" height="1" fill="{border_color}" />
                <g transform="translate(0, 20)">
"""

    socials = ["GitHub", "LinkedIn", "Twitter", "Portfolio"]
    for i, social in enumerate(socials):
        svg += f'                    <g transform="translate({i * 120}, 0)" opacity="0">\n'
        svg += f'                        <animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" dur="100s" begin="{7 + i*0.3}s" fill="freeze" />\n'
        svg += f'                        <text x="0" y="15" fill="{text_muted}" font-size="14" font-weight="bold">\n'
        svg += f'                            <tspan>↗ </tspan>\n'
        svg += f'                            <tspan fill="{text_primary}">{social}</tspan>\n'
        svg += f'                        </text>\n'
        svg += f'                    </g>\n'

    svg += f"""                </g>
            </g>
            
        </g>
    </g>
</svg>"""

    with open(f"{mode}.svg", "w") as f:
        f.write(svg)

generate_svg('dark')
generate_svg('light')
print("SVGs generated successfully!")
