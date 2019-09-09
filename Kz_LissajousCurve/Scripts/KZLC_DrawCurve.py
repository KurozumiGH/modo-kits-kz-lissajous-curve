# python
# -*- coding: utf-8 -*-

import lx
import math
import KZLC_Math as kzm

# Note: V-Ray curve settings
# item.channel vray_curve_max_segments 5000 (points * 2..3)

# Get parameters.
points = lx.eval('user.value kzlc.points ?')
center_x = lx.eval('user.value kzlc.center_x ?')
center_y = lx.eval('user.value kzlc.center_y ?')
center_z = lx.eval('user.value kzlc.center_z ?')
scale_x = lx.eval('user.value kzlc.scale_x ?') / 2.0
scale_y = lx.eval('user.value kzlc.scale_y ?') / 2.0
scale_z = lx.eval('user.value kzlc.scale_z ?') / 2.0
freq_x = lx.eval('user.value kzlc.freq_x ?')
freq_y = lx.eval('user.value kzlc.freq_y ?')
freq_z = lx.eval('user.value kzlc.freq_z ?')
phase_x = lx.eval('user.value kzlc.phase_x ?') * kzm.PI2
phase_y = lx.eval('user.value kzlc.phase_y ?') * kzm.PI2
phase_z = lx.eval('user.value kzlc.phase_z ?') * kzm.PI2

# Generate angles.
angles = kzm.linspace(0.0, kzm.PI2, points)

# Start curve.
lx.eval('tool.set prim.curve on')
lx.eval('tool.setAttr prim.curve mode add')

# Set curve points.
pointIdx = 0
for a in angles:
    pointIdx = pointIdx + 1

    # Calc point location.
    x = center_x + scale_x * math.cos(a * freq_x + phase_x)
    y = center_y + scale_y * math.sin(a * freq_y + phase_y)
    z = center_z + scale_z * math.sin(a * freq_z + phase_z)

    # Set point.
    lx.eval('tool.setAttr prim.curve number %s' % pointIdx)
    lx.eval('tool.setAttr prim.curve ptX %s' % x)
    lx.eval('tool.setAttr prim.curve ptY %s' % y)
    lx.eval('tool.setAttr prim.curve ptZ %s' % z)

# End curve.
lx.eval('tool.doApply')
lx.eval('tool.set prim.curve off 0')
