# Flow-Speed Measurement in a Tube

## Detailed theory and measurement guide for the Fizika laboratórium 1 assignment

**Assignment topic:** *Áramlási sebesség mérése csőben* — measuring the flow velocity of a liquid through a small tube.  
**Core task:** build a PET-bottle based flow device, calibrate the hydrostatic pressure, measure outflow speed for different pressures and tube lengths, analyze the results, and determine the viscosity of water.  
**Recommended primary analysis:** measure the volume flow rate \(Q\), calculate the average tube velocity \(v=Q/A\), and use Hagen-Poiseuille theory plus uncertainty analysis.

---

# 1. What you have to achieve

The assignment has three main experimental parts.

## 1.1 Build the device

You need a measuring device that can measure the outflow speed for different tube lengths. The assignment suggests:

- a cylindrical PET bottle;
- a small drilled hole;
- a small tube, for example a straw or capillary tube, with diameter at most about 3 mm;
- glue or sealant to make the joint watertight.

The tube should be mounted horizontally near the lower side of the bottle. The water level above the tube creates the hydrostatic pressure that drives the flow.

## 1.2 Calibrate the device

For calibration:

1. Close the outlet.
2. Fill the bottle with different amounts of water.
3. Mark the water levels on the bottle.
4. Measure the height difference \(h\) between each water level and the centerline of the tube.
5. Calculate the hydrostatic pressure for each marked level:

\[
\Delta p = \rho g h.
\]

## 1.3 Perform the measurements

At **basic level** you need to:

1. Measure outflow velocity as a function of hydrostatic pressure for one chosen tube length.
2. Repeat each pressure point at least 2-3 times.
3. Repeat the measurement for at least 10 different tube lengths between about 5 mm and 50 cm.
4. Plot and analyze the data.
5. Draw conclusions.
6. Determine the viscosity of water.

At **advanced level** you also need to choose an extra parameter study, for example:

- different liquids, such as oil or dishwashing liquid;
- different solution concentrations, such as sugar-water or detergent-water mixtures;
- different water temperatures, for example from near \(0^\circ\mathrm{C}\) to about \(40-50^\circ\mathrm{C}\).

Then you should compare your results with theory and with literature values.

---

# 2. Physical quantities and notation

| Symbol | Meaning | Unit |
|---|---|---|
| \(h\) | height difference between water surface and tube centerline | m |
| \(\Delta p\) | pressure difference driving the flow | Pa |
| \(\rho\) | liquid density | kg/m\(^3\) |
| \(g\) | gravitational acceleration, approximately \(9.81\,\mathrm{m/s^2}\) | m/s\(^2\) |
| \(L\) | tube length | m |
| \(d\) | inner tube diameter | m |
| \(r=d/2\) | inner tube radius | m |
| \(A=\pi r^2\) | tube cross-sectional area | m\(^2\) |
| \(V\) | collected liquid volume | m\(^3\) |
| \(t\) | collection time | s |
| \(Q=V/t\) | volume flow rate | m\(^3\)/s |
| \(v=Q/A\) | average flow speed in tube | m/s |
| \(\eta\) | dynamic viscosity | Pa s |
| \(\nu=\eta/\rho\) | kinematic viscosity | m\(^2\)/s |
| \(\mathrm{Re}\) | Reynolds number | dimensionless |

Approximate useful values for water near room temperature:

\[
\rho_\mathrm{water}\approx 998\,\mathrm{kg/m^3},
\qquad
\eta_\mathrm{water}(20^\circ\mathrm{C})\approx 1.00\times 10^{-3}\,\mathrm{Pa\,s}.
\]

The viscosity of water changes noticeably with temperature, so you should measure the water temperature if you want to compare with a literature value.

---

# 3. Hydrostatic pressure: the calibration theory

The water column above the tube produces a pressure difference. If the bottle is open at the top and the tube outlet is open to the air, then the pressure difference between the tube inlet and the outside air is approximately

\[
\Delta p = \rho g h.
\]

Here \(h\) is the vertical distance from the free water surface to the center of the tube.

## 3.1 What exactly should be measured?

Measure \(h\) like this:

\[
 h = \text{height of water surface} - \text{height of tube centerline}.
\]

Do **not** measure from the table or from the bottom of the bottle. The tube centerline is the natural zero level for hydrostatic pressure.

## 3.2 Useful pressure conversion

For water,

\[
1\,\mathrm{cm}\ \text{water column} \approx 98.1\,\mathrm{Pa}.
\]

So if \(h=10\,\mathrm{cm}\), then

\[
\Delta p \approx 981\,\mathrm{Pa}.
\]

If \(h=25\,\mathrm{cm}\), then

\[
\Delta p \approx 2450\,\mathrm{Pa}.
\]

## 3.3 Calibration table template

| Mark number | Height \(h\) above tube center / cm | Height \(h\) / m | \(\Delta p=\rho gh\) / Pa | Notes |
|---:|---:|---:|---:|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |

Recommended: use at least 5-8 different water levels. More levels give better plots.

---

# 4. Bernoulli equation and Torricelli's law

## 4.1 Ideal-fluid prediction

For an ideal fluid flowing out of a large container through a very short hole, Bernoulli's equation gives

\[
\rho g h = \frac{1}{2}\rho v^2.
\]

Therefore

\[
 v = \sqrt{2gh}.
\]

This is **Torricelli's law**.

In terms of pressure:

\[
 v = \sqrt{\frac{2\Delta p}{\rho}}.
\]

So the ideal prediction is

\[
 v \propto \sqrt{h}
 \quad\text{and}\quad
 v^2 \propto h.
\]

## 4.2 Why this is only a reference model

Your tube is not just a hole. It is a narrow channel with walls. Real water has viscosity, so friction at the wall causes energy loss. Therefore the measured velocity is usually less than Torricelli's ideal prediction.

Torricelli's law is useful as a **comparison curve**, especially for very short tubes, but it will not usually describe long narrow tubes well.

## 4.3 What to plot from the Bernoulli viewpoint

For each tube length, you can plot:

1. \(v\) versus \(h\);
2. \(v\) versus \(\sqrt{h}\);
3. \(v^2\) versus \(h\).

If Torricelli behavior dominates, \(v^2\) versus \(h\) should be approximately linear.

---

# 5. Viscous flow and the Hagen-Poiseuille law

## 5.1 Main idea

For slow, laminar, incompressible flow through a long circular tube, the Hagen-Poiseuille law states:

\[
Q = \frac{\pi r^4}{8\eta L}\Delta p.
\]

Here:

- \(Q\) is the volume flow rate;
- \(r\) is the inner radius of the tube;
- \(L\) is the tube length;
- \(\eta\) is the dynamic viscosity;
- \(\Delta p\) is the pressure difference.

The average velocity in the tube is

\[
 v = \frac{Q}{A}=\frac{Q}{\pi r^2}.
\]

Substituting \(Q\) gives

\[
 v = \frac{r^2}{8\eta L}\Delta p.
\]

Since \(\Delta p=\rho gh\), this becomes

\[
 v = \frac{\rho g r^2}{8\eta L}h.
\]

So in laminar Poiseuille flow:

\[
 v \propto \Delta p,
\qquad
v \propto h,
\qquad
v \propto \frac{1}{L},
\qquad
v \propto r^2.
\]

For volume flow rate:

\[
Q \propto \Delta p,
\qquad
Q \propto \frac{1}{L},
\qquad
Q \propto r^4.
\]

The \(r^4\) dependence is extremely important: a small uncertainty in tube radius causes a large uncertainty in the calculated viscosity.

## 5.2 Velocity profile inside the tube

In laminar Poiseuille flow, the velocity is not uniform across the tube. It is parabolic:

\[
 u(s)=u_\mathrm{max}\left(1-\frac{s^2}{r^2}\right),
\]

where \(s\) is the radial distance from the tube center.

The average velocity is half the maximum centerline velocity:

\[
 v_\mathrm{avg}=\frac{u_\mathrm{max}}{2}.
\]

If you measure flow by collecting volume, you get \(Q\), and then \(v=Q/A\) is the **average** tube velocity. This is the best quantity for Hagen-Poiseuille analysis.

## 5.3 Hydraulic resistance form

It is often cleaner to write the equation as

\[
\Delta p = RQ,
\]

where the hydraulic resistance of a cylindrical tube is

\[
R = \frac{8\eta L}{\pi r^4}.
\]

This suggests a very good way to determine viscosity:

1. For each tube length, measure \(Q\) at several pressures.
2. For each tube length, fit a line to \(\Delta p\) versus \(Q\).
3. The slope is the hydraulic resistance \(R\).
4. Plot \(R\) versus \(L\).
5. The slope of that graph should be

\[
\frac{dR}{dL}=\frac{8\eta}{\pi r^4}.
\]

Therefore

\[
\eta = \frac{\pi r^4}{8}\frac{dR}{dL}.
\]

This is one of the most robust analysis methods because it uses all tube lengths together.

## 5.4 End correction and non-ideal losses

Real short tubes may not follow the simple \(R\propto L\) relation because there are additional losses at the entrance and exit. A useful empirical model is

\[
R = \frac{8\eta}{\pi r^4}(L+L_0),
\]

where \(L_0\) is an effective extra length representing entrance/exit effects.

If you plot \(R\) versus \(L\), then:

- the slope gives viscosity;
- the intercept tells you about extra losses;
- short tubes may deviate more strongly from the line.

For this reason, do not rely only on the shortest tubes when determining viscosity.

---

# 6. Laminar versus turbulent flow: Reynolds number

The Hagen-Poiseuille law is valid for laminar flow. To check whether this is reasonable, calculate the Reynolds number:

\[
\mathrm{Re}=\frac{\rho v d}{\eta}.
\]

For pipe flow:

- \(\mathrm{Re}\lesssim 2000\): usually laminar;
- \(\mathrm{Re}\gtrsim 2000\): transition or turbulent behavior may appear.

This threshold is not exact for your homemade device, but it is a useful warning.

## 6.1 Example estimate

Suppose:

- \(d=3\,\mathrm{mm}=0.003\,\mathrm{m}\),
- \(v=0.5\,\mathrm{m/s}\),
- \(\rho=1000\,\mathrm{kg/m^3}\),
- \(\eta=1.0\times10^{-3}\,\mathrm{Pa\,s}\).

Then

\[
\mathrm{Re}=\frac{1000\cdot0.5\cdot0.003}{10^{-3}}=1500.
\]

This is still likely laminar or near transition. But if \(v=1\,\mathrm{m/s}\), then

\[
\mathrm{Re}=3000,
\]

which may be transitional or turbulent.

## 6.2 Practical advice

To keep flow closer to laminar:

- use lower water heights;
- use longer tubes;
- use smaller tube diameter;
- avoid very rough or irregular tubes;
- avoid sudden bends;
- ensure the tube is clean and not partially blocked.

In your report, calculate \(\mathrm{Re}\) for representative data points. If some data have high Reynolds number, mention that Hagen-Poiseuille theory may not apply perfectly there.

---

# 7. How to measure the flow speed

There are two practical methods. The **volume-time method** is recommended as the main method because it directly gives \(Q\), which is exactly what Poiseuille theory uses.

---

## 7.1 Method A: collect volume over time — recommended

Collect water from the tube outlet into a measuring cylinder or onto a scale for a measured time interval.

### Step-by-step

1. Choose tube length \(L\).
2. Fill the bottle to a marked water level.
3. Open the outlet.
4. Start timing when the flow becomes steady.
5. Collect water for a fixed time \(t\), for example 10-30 s.
6. Measure collected volume \(V\), or measure mass \(m\) and convert using \(V=m/\rho\).
7. Calculate

\[
Q=\frac{V}{t}.
\]

8. Calculate the average velocity:

\[
 v=\frac{Q}{A}=\frac{Q}{\pi r^2}.
\]

### Important detail: pressure changes during the measurement

As water flows out, the water level decreases, so \(h\) and \(\Delta p\) decrease.

There are three ways to handle this:

### Option 1: keep the collected volume small

Choose short collection intervals so that the water level changes only slightly. Then use the initial or average height.

Better:

\[
 h_\mathrm{avg}=\frac{h_\mathrm{start}+h_\mathrm{end}}{2}.
\]

Then

\[
\Delta p_\mathrm{avg}=\rho g h_\mathrm{avg}.
\]

### Option 2: keep water level approximately constant

Use a large bottle and collect only a small fraction of the total volume. This makes \(h\) nearly constant.

### Option 3: record start and end level carefully

For each run, record both \(h_\mathrm{start}\) and \(h_\mathrm{end}\). This is better documentation and improves uncertainty analysis.

---

## 7.2 Method B: projectile range method — optional check

If the tube exits horizontally, the water jet follows projectile motion. If the outlet is at height \(y\) above the landing surface and the jet lands horizontal distance \(x\) away, then the fall time is

\[
 t_\mathrm{fall}=\sqrt{\frac{2y}{g}}.
\]

The horizontal exit speed is approximately

\[
 v=\frac{x}{t_\mathrm{fall}}=x\sqrt{\frac{g}{2y}}.
\]

This is useful as a visual check, but it can be less reliable because:

- the jet breaks into droplets;
- the landing point is hard to define;
- the jet may not be perfectly horizontal;
- the tube exit profile may not correspond to a single speed;
- splashing causes uncertainty.

If you use this method, include photos or video frames and estimate uncertainty in \(x\) and \(y\).

---

# 8. Device construction guide

## 8.1 Materials

Suggested materials:

- cylindrical PET bottle;
- thin tube or straw, inner diameter at most about 3 mm;
- glue gun, epoxy, silicone, or waterproof sealant;
- drill or heated needle for making the hole;
- ruler or caliper;
- measuring cylinder or kitchen scale;
- stopwatch or phone video;
- clamp or tape to hold bottle steady;
- marker pen for water levels;
- container to collect water;
- thermometer, especially for advanced temperature measurements.

## 8.2 Tube mounting

The tube should be:

- horizontal;
- tightly sealed;
- straight, if possible;
- not squeezed or deformed by glue;
- mounted at a known height.

Important: the **inner diameter** matters, not the outer diameter. If you only measure outer diameter, your viscosity estimate can be badly wrong.

## 8.3 How to make tube length variable

Possible designs:

### Design A: interchangeable tubes

Prepare several tubes with different lengths and insert them one at a time into the same bottle hole. Seal with removable putty, silicone, or a tight adapter.

Pros:

- easiest to understand;
- clean comparison between lengths.

Cons:

- sealing may vary between tubes;
- repeated assembly may damage the hole.

### Design B: one long tube cut gradually shorter

Start with a long tube, perform measurements, then cut it shorter and repeat.

Pros:

- same tube diameter throughout;
- good for comparing length dependence.

Cons:

- cannot return to previous lengths;
- need careful length measurement after each cut.

### Design C: tube with external extensions

Use a short fixed connector in the bottle and attach external tubes of different lengths.

Pros:

- bottle seal remains unchanged;
- convenient for many lengths.

Cons:

- connectors add extra losses;
- diameter mismatch can disturb the flow.

Best recommendation: use **Design B** or **Design C**, and document exactly what you did.

## 8.4 Leak test

Before real measurements:

1. Fill the bottle.
2. Close the outlet.
3. Check whether water leaks around the glued joint.
4. Open the tube and watch whether the jet is stable.
5. Repeat after changing tube length.

If there is leakage, the pressure and flow rate are not well defined. Fix the seal before measuring.

---

# 9. Calibration procedure in detail

## 9.1 Marking levels

1. Place the empty bottle upright on a stable surface.
2. Mark the tube centerline on the bottle wall.
3. Close the outlet.
4. Add water to a chosen level.
5. Wait until the water surface is calm.
6. Mark the water level.
7. Measure the vertical distance from the tube centerline to the water surface.
8. Repeat for several levels.

## 9.2 Pressure calculation

For each level:

\[
\Delta p_i = \rho g h_i.
\]

If using water at room temperature, \(\rho\approx 998\,\mathrm{kg/m^3}\) is enough for most school/lab-level analysis.

## 9.3 Calibration uncertainty

If your ruler uncertainty is \(\delta h\), then

\[
\delta(\Delta p)=\rho g\,\delta h.
\]

Relative uncertainty:

\[
\frac{\delta(\Delta p)}{\Delta p}=\frac{\delta h}{h}.
\]

This means low water levels have larger relative pressure uncertainty. Avoid extremely small \(h\) values if possible.

---

# 10. Basic measurement A: speed versus pressure for one tube length

## 10.1 Aim

For a fixed tube length \(L\), measure how the average outflow speed depends on hydrostatic pressure.

You want to test whether the relation looks more like:

- ideal/Torricelli behavior:

\[
 v\propto \sqrt{\Delta p},
\]

or laminar/Poiseuille behavior:

\[
 v\propto \Delta p.
\]

## 10.2 Procedure

1. Choose one tube length, for example \(L=10\,\mathrm{cm}\) or \(L=20\,\mathrm{cm}\).
2. Measure the inner diameter \(d\) of the tube.
3. Calculate \(A=\pi(d/2)^2\).
4. Choose at least 5-8 water-level marks.
5. For each water level:
   - fill the bottle to the mark;
   - record \(h_\mathrm{start}\);
   - open the outlet;
   - collect water for time \(t\);
   - record collected volume \(V\) or mass \(m\);
   - record \(h_\mathrm{end}\), if possible;
   - repeat 2-3 times.
6. Calculate average pressure:

\[
 h_\mathrm{avg}=\frac{h_\mathrm{start}+h_\mathrm{end}}{2},
\qquad
\Delta p_\mathrm{avg}=\rho g h_\mathrm{avg}.
\]

7. Calculate

\[
Q=\frac{V}{t},
\qquad
v=\frac{Q}{A}.
\]

## 10.3 Data table template

| Tube length \(L\) / cm | Trial | \(h_\mathrm{start}\) / cm | \(h_\mathrm{end}\) / cm | \(h_\mathrm{avg}\) / cm | \(\Delta p\) / Pa | Time \(t\) / s | Volume \(V\) / mL | \(Q\) / mL/s | \(v\) / m/s |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | 1 |  |  |  |  |  |  |  |  |
|  | 2 |  |  |  |  |  |  |  |  |
|  | 3 |  |  |  |  |  |  |  |  |

## 10.4 Plots

Make at least these plots:

1. \(v\) versus \(\Delta p\);
2. \(Q\) versus \(\Delta p\);
3. \(v^2\) versus \(h\), as a Torricelli check.

For Poiseuille flow, \(Q\) versus \(\Delta p\) should be approximately linear:

\[
Q = S\Delta p,
\]

where

\[
S=\frac{\pi r^4}{8\eta L}.
\]

Then viscosity from one tube length is

\[
\eta = \frac{\pi r^4}{8LS}.
\]

However, this single-length estimate is less robust than the multi-length resistance method described later.

---

# 11. Basic measurement B: measurements for at least 10 tube lengths

## 11.1 Aim

Measure how the flow depends on tube length. Hagen-Poiseuille theory predicts

\[
Q \propto \frac{1}{L}
\]

at fixed pressure.

Equivalently, hydraulic resistance should be proportional to length:

\[
R=\frac{\Delta p}{Q}\propto L.
\]

## 11.2 Choosing tube lengths

The assignment asks for at least 10 tube lengths between about 5 mm and 50 cm.

A possible set:

| Index | Tube length |
|---:|---:|
| 1 | 0.5 cm |
| 2 | 1 cm |
| 3 | 2 cm |
| 4 | 3 cm |
| 5 | 5 cm |
| 6 | 7.5 cm |
| 7 | 10 cm |
| 8 | 15 cm |
| 9 | 25 cm |
| 10 | 50 cm |

Better for fitting: include several longer tubes, because very short tubes may be dominated by entrance/exit losses.

A more analysis-friendly set might be:

\[
L = 2,\ 4,\ 6,\ 8,\ 10,\ 15,\ 20,\ 30,\ 40,\ 50\ \mathrm{cm}.
\]

You can still include a very short tube as an interesting comparison.

## 11.3 Measurement procedure for each length

For each tube length:

1. Measure and record \(L\).
2. Check that the tube is sealed and not blocked.
3. Use the same calibration marks as before.
4. Measure flow for several pressure values.
5. Repeat each pressure value 2-3 times.
6. Calculate \(Q\), \(v\), and \(R=\Delta p/Q\).
7. Calculate Reynolds number for representative points.

## 11.4 Data table template for multi-length measurement

| Tube length \(L\) / cm | Pressure point | Trial | \(h_\mathrm{avg}\) / cm | \(\Delta p\) / Pa | \(t\) / s | \(V\) / mL | \(Q\) / mL/s | \(v\) / m/s | \(R=\Delta p/Q\) / Pa s/m\(^3\) | Re |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  |  | 1 |  |  |  |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |  |  |
|  |  | 3 |  |  |  |  |  |  |  |  |

## 11.5 Recommended analysis workflow

For each tube length:

1. Average repeated measurements at the same pressure.
2. Plot \(Q\) versus \(\Delta p\).
3. Fit a straight line:

\[
Q = S_L\Delta p + b.
\]

Ideally \(b\approx 0\), because no pressure difference should mean no flow. In practice, a small intercept can appear because of timing, reading, or sealing errors.

4. The slope \(S_L\) is the conductance:

\[
S_L = \frac{Q}{\Delta p}.
\]

5. The resistance is

\[
R_L=\frac{1}{S_L}.
\]

6. Plot \(R_L\) versus \(L\).
7. Fit a line:

\[
R_L = aL+c.
\]

8. Determine viscosity from the slope:

\[
\eta = \frac{a\pi r^4}{8}.
\]

This is probably the best final value for water viscosity.

---

# 12. Basic measurement C: analysis, conclusions, and viscosity

## 12.1 Main plots to include

You should include plots that answer the assignment questions clearly.

### Plot 1: calibration plot

Plot

\[
\Delta p
\quad\text{versus}\quad
h.
\]

This should be a straight line with slope \(\rho g\). This plot demonstrates your calibration.

### Plot 2: speed or flow rate versus pressure for one tube length

Plot

\[
Q\quad\text{versus}\quad\Delta p
\]

and/or

\[
v\quad\text{versus}\quad\Delta p.
\]

This tests Poiseuille behavior.

### Plot 3: Torricelli comparison

Plot measured \(v\) together with

\[
v_\mathrm{ideal}=\sqrt{2gh}.
\]

This shows how much slower the real viscous flow is compared with ideal outflow.

### Plot 4: length dependence

At fixed pressure, plot

\[
Q\quad\text{versus}\quad\frac{1}{L}.
\]

Poiseuille theory predicts this should be approximately linear for sufficiently long tubes.

### Plot 5: hydraulic resistance versus tube length

Plot

\[
R=\frac{\Delta p}{Q}
\quad\text{versus}\quad
L.
\]

This is the best plot for determining viscosity.

## 12.2 Determining viscosity from one tube length

If you use one fixed tube length and fit

\[
Q=S\Delta p,
\]

then

\[
S=\frac{\pi r^4}{8\eta L}.
\]

So

\[
\boxed{\eta = \frac{\pi r^4}{8LS}}.
\]

This method is simple, but it is sensitive to errors and non-ideal losses.

## 12.3 Determining viscosity from many tube lengths

For each tube length, estimate

\[
R_L=\frac{\Delta p}{Q}.
\]

Then fit

\[
R_L=aL+c.
\]

The slope should be

\[
a=\frac{8\eta}{\pi r^4}.
\]

Therefore

\[
\boxed{\eta=\frac{a\pi r^4}{8}}.
\]

This method is recommended.

## 12.4 What conclusions should you discuss?

Your discussion should answer questions such as:

1. Does \(Q\) increase linearly with \(\Delta p\)?
2. Does \(v\) increase linearly with \(h\), as Poiseuille theory predicts?
3. Does \(v\) increase like \(\sqrt{h}\), as Torricelli theory predicts?
4. Which model describes the data better?
5. Does resistance increase linearly with tube length?
6. Are the shortest tubes outliers?
7. What viscosity do you obtain?
8. How close is it to the literature value for water at your measured temperature?
9. What is the largest source of uncertainty?
10. Were there signs of turbulent or transitional flow?

---

# 13. Advanced-level extra studies

The advanced level requires one extra parameter study. Choose the option that is easiest to perform carefully and safely.

---

## 13.1 Option A: temperature dependence of water viscosity — recommended

This is probably the cleanest advanced option.

### Theory

The viscosity of water decreases as temperature increases. Therefore at the same pressure and tube length, warmer water should flow faster.

Poiseuille law predicts

\[
Q = \frac{\pi r^4}{8\eta(T)L}\Delta p.
\]

So if \(\eta(T)\) decreases, \(Q\) increases.

### Procedure

1. Choose one or two tube lengths, preferably medium/long lengths.
2. Choose several water temperatures, for example:

\[
5^\circ\mathrm{C},\ 15^\circ\mathrm{C},\ 25^\circ\mathrm{C},\ 35^\circ\mathrm{C},\ 45^\circ\mathrm{C}.
\]

3. Measure the actual temperature before and after each run.
4. Use the same pressure levels for every temperature.
5. Calculate \(Q\), \(v\), and \(\eta\) for each temperature.
6. Plot \(\eta\) versus temperature.
7. Compare with literature values.

### Expected result

Warmer water should have smaller viscosity and therefore larger flow rate.

Approximate reference values for water:

| Temperature | Approximate dynamic viscosity of water |
|---:|---:|
| \(0^\circ\mathrm{C}\) | \(1.79\times10^{-3}\,\mathrm{Pa\,s}\) |
| \(10^\circ\mathrm{C}\) | \(1.31\times10^{-3}\,\mathrm{Pa\,s}\) |
| \(20^\circ\mathrm{C}\) | \(1.00\times10^{-3}\,\mathrm{Pa\,s}\) |
| \(30^\circ\mathrm{C}\) | \(0.80\times10^{-3}\,\mathrm{Pa\,s}\) |
| \(40^\circ\mathrm{C}\) | \(0.65\times10^{-3}\,\mathrm{Pa\,s}\) |
| \(50^\circ\mathrm{C}\) | \(0.55\times10^{-3}\,\mathrm{Pa\,s}\) |

Use a real source in the final report and cite it properly. The table above is only a rough guide.

---

## 13.2 Option B: different liquids

Possible liquids:

- water;
- sugar-water solution;
- vegetable oil;
- diluted dishwashing liquid.

### Theory

Higher-viscosity liquids flow more slowly. For the same tube and pressure:

\[
Q\propto \frac{1}{\eta}.
\]

So if oil is much more viscous than water, it should have a much smaller flow rate.

### Important warning

Liquids such as dishwashing liquid may be non-Newtonian or may foam. Hagen-Poiseuille theory assumes a Newtonian fluid with constant viscosity. If the liquid is non-Newtonian, the apparent viscosity may depend on flow speed.

### Procedure

1. Use one or two tube lengths.
2. Use the same pressure levels for each liquid.
3. Measure density if possible, especially for oil or concentrated sugar water.
4. Measure \(Q\) carefully.
5. Estimate apparent viscosity using Poiseuille law.
6. Compare the relative viscosities:

\[
\frac{\eta_1}{\eta_2} = \frac{Q_2}{Q_1}
\]

if the same tube and pressure are used.

---

## 13.3 Option C: concentration dependence

Example: sugar-water solutions of different concentrations.

### Theory

Increasing sugar concentration usually increases viscosity and density. The pressure is

\[
\Delta p=\rho g h,
\]

so the density change affects the driving pressure. The viscosity affects the resistance.

For each solution, use

\[
Q = \frac{\pi r^4}{8\eta L}\rho g h.
\]

### Procedure

1. Prepare solutions with known mass fraction, for example 0%, 5%, 10%, 15%, 20% sugar by mass.
2. Record exactly how each solution was made.
3. Measure or estimate density.
4. Use the same tube length and water-level marks.
5. Determine apparent viscosity.
6. Plot viscosity versus concentration.

### Expected result

Higher concentration should usually mean higher viscosity and lower flow rate.

---

# 14. Uncertainty analysis

A strong lab report must discuss measurement errors. This assignment explicitly expects careful measurement, error determination, and repeated measurements.

---

## 14.1 Pressure uncertainty

\[
\Delta p=\rho gh.
\]

If density and \(g\) are treated as exact compared with height uncertainty, then

\[
\delta(\Delta p)=\rho g\delta h.
\]

Relative uncertainty:

\[
\frac{\delta(\Delta p)}{\Delta p}\approx \frac{\delta h}{h}.
\]

Example: if \(h=10\,\mathrm{cm}\) and \(\delta h=1\,\mathrm{mm}=0.1\,\mathrm{cm}\), then

\[
\frac{\delta h}{h}=\frac{0.1}{10}=1\%.
\]

---

## 14.2 Volume flow rate uncertainty

\[
Q=\frac{V}{t}.
\]

Relative uncertainty:

\[
\frac{\delta Q}{Q}
\approx
\sqrt{\left(\frac{\delta V}{V}\right)^2+
\left(\frac{\delta t}{t}\right)^2}.
\]

To reduce uncertainty:

- collect a larger volume;
- use longer collection times;
- use a scale instead of reading a small measuring cylinder;
- repeat measurements.

If using mass measurement:

\[
V=\frac{m}{\rho}.
\]

A kitchen scale with 1 g resolution gives about 1 mL resolution for water.

---

## 14.3 Tube radius uncertainty — usually the most important

The Poiseuille formula contains \(r^4\):

\[
Q = \frac{\pi r^4}{8\eta L}\Delta p.
\]

Therefore the relative uncertainty contribution from radius is approximately

\[
\frac{\delta(r^4)}{r^4}=4\frac{\delta r}{r}.
\]

Example: if \(r=1.5\,\mathrm{mm}\) and \(\delta r=0.05\,\mathrm{mm}\), then

\[
4\frac{\delta r}{r}=4\frac{0.05}{1.5}\approx 13\%.
\]

So radius measurement can dominate the final viscosity error.

### How to improve radius measurement

- Use a caliper if possible.
- Measure the inner diameter at several positions.
- If possible, photograph the tube cross-section next to a ruler and analyze the image.
- Avoid tubes that are oval, squeezed, or rough.
- Use the same tube for all lengths if possible.

---

## 14.4 Viscosity uncertainty from single-length method

For

\[
\eta = \frac{\pi r^4}{8LS},
\]

where \(S\) is the slope of \(Q\) versus \(\Delta p\), the relative uncertainty is approximately

\[
\frac{\delta\eta}{\eta}
\approx
\sqrt{
\left(4\frac{\delta r}{r}\right)^2+
\left(\frac{\delta L}{L}\right)^2+
\left(\frac{\delta S}{S}\right)^2
}.
\]

Usually \(4\delta r/r\) is large.

---

## 14.5 Random and systematic errors

### Random errors

Random errors vary from trial to trial. Examples:

- reaction time when using stopwatch;
- reading the water level;
- small fluctuations in the jet;
- volume reading uncertainty.

Handle these by repeated measurements and standard deviation.

### Systematic errors

Systematic errors shift all measurements in one direction. Examples:

- wrong tube diameter;
- leak near the tube;
- tube not horizontal;
- water level changes significantly during measurement;
- unaccounted entrance/exit losses;
- assuming room-temperature viscosity when water temperature is different.

Systematic errors are often more dangerous because repeating the same wrong measurement does not remove them.

---

# 15. Data analysis plan

This section gives a practical analysis pipeline that you can follow directly.

---

## 15.1 Raw data preparation

For each trial, record:

- tube length \(L\);
- tube inner diameter \(d\);
- liquid temperature \(T\);
- starting height \(h_\mathrm{start}\);
- ending height \(h_\mathrm{end}\);
- collection time \(t\);
- collected volume \(V\) or mass \(m\);
- notes about problems, leaks, bubbles, jet instability, etc.

Then calculate:

\[
h_\mathrm{avg}=\frac{h_\mathrm{start}+h_\mathrm{end}}{2},
\]

\[
\Delta p=\rho gh_\mathrm{avg},
\]

\[
Q=\frac{V}{t},
\]

\[
A=\pi r^2,
\]

\[
v=\frac{Q}{A},
\]

\[
\mathrm{Re}=\frac{\rho vd}{\eta_\mathrm{ref}}.
\]

For the Reynolds number, you can initially use \(\eta_\mathrm{ref}=1.0\times10^{-3}\,\mathrm{Pa\,s}\) for water near room temperature, then update it after you estimate viscosity.

---

## 15.2 Repeated measurements

For repeated trials at the same \(L\) and pressure:

1. Calculate \(Q\) for each trial.
2. Calculate the mean:

\[
\bar Q=\frac{1}{n}\sum_{i=1}^n Q_i.
\]

3. Calculate the standard deviation:

\[
s_Q=\sqrt{\frac{1}{n-1}\sum_{i=1}^n(Q_i-\bar Q)^2}.
\]

4. Use error bars if possible.

With only 2-3 repetitions, the standard deviation estimate is rough, but it is still better than no uncertainty estimate.

---

## 15.3 Linear fits

For each tube length, fit

\[
Q = S_L\Delta p + b.
\]

Record:

- slope \(S_L\);
- intercept \(b\);
- uncertainty of slope;
- \(R^2\) or some measure of goodness of fit;
- whether the intercept is small compared with measured flow rates.

Then calculate

\[
R_L=\frac{1}{S_L}.
\]

Finally fit

\[
R_L=aL+c.
\]

Use

\[
\eta=\frac{a\pi r^4}{8}.
\]

---

# 16. Expected qualitative results

## 16.1 Pressure dependence

For long narrow tubes and laminar flow:

\[
Q\propto \Delta p,
\qquad
v\propto \Delta p.
\]

So the graph of \(Q\) versus \(\Delta p\) should be approximately a straight line.

For ideal outflow through a short hole:

\[
v\propto \sqrt{\Delta p}.
\]

So short tubes may show weaker-than-linear pressure dependence.

## 16.2 Length dependence

For Poiseuille flow:

\[
Q\propto \frac{1}{L}.
\]

So longer tubes give smaller flow rates.

Hydraulic resistance should increase linearly:

\[
R\propto L.
\]

## 16.3 Diameter dependence

If you accidentally use tubes with slightly different diameters, the results may change strongly because

\[
Q\propto r^4.
\]

This is why using the same tube and cutting it shorter can be better than using many different straws.

---

# 17. Common experimental problems and fixes

## 17.1 Water level drops too much during measurement

Problem: pressure is not constant.  
Fix: collect for a shorter time or use a larger bottle. Record start and end heights and use \(h_\mathrm{avg}\).

## 17.2 Jet is unstable or splashes

Problem: hard to measure volume or projectile range.  
Fix: use volume-time method, collect water directly into a container, avoid measuring tiny volumes.

## 17.3 Tube leaks at bottle wall

Problem: actual flow is not only through the tube.  
Fix: reseal and repeat measurements.

## 17.4 Tube diameter is uncertain

Problem: viscosity estimate becomes unreliable.  
Fix: measure inner diameter carefully at multiple locations. State the uncertainty honestly.

## 17.5 Flow may be turbulent

Problem: Poiseuille law may fail.  
Fix: calculate Reynolds number. Use lower heights or longer tubes. Discuss deviations.

## 17.6 Short tubes do not fit the line

Problem: entrance/exit losses dominate.  
Fix: mention end effects. Determine viscosity mainly from longer tubes.

## 17.7 Air bubbles in tube

Problem: effective cross-section changes and flow is unstable.  
Fix: flush the tube before measuring.

---

# 18. Recommended report structure

Use a clear report structure. The grading criteria emphasize good documentation and conclusions supported by data.

## 18.1 Title

Example:

**Measurement of flow velocity in a narrow tube and determination of water viscosity**

## 18.2 Abstract

Mention:

- what you measured;
- whether you completed basic or advanced level;
- main method;
- main result for water viscosity;
- main conclusion.

Example abstract skeleton:

> In this experiment I built and calibrated a PET-bottle flow device to measure the average outflow velocity of water through narrow tubes of different lengths. The hydrostatic pressure was determined from the water height above the tube, and flow rate was measured by collecting water over time. Measurements were performed for ... tube lengths and ... pressure values. The data were compared with Bernoulli/Torricelli and Hagen-Poiseuille predictions. From the slope of hydraulic resistance versus tube length, the dynamic viscosity of water was found to be ... Pa s at ... °C. The results show ...

Important: the assignment says the abstract should make clear which difficulty level you chose.

## 18.3 Introduction and theory

Include:

- hydrostatic pressure;
- Bernoulli equation and Torricelli law;
- Hagen-Poiseuille law;
- Reynolds number;
- expected dependencies.

## 18.4 Apparatus and calibration

Include:

- photo of device;
- drawing or schematic;
- tube diameter and length measurement;
- how tube lengths were varied;
- calibration marks;
- calibration table;
- uncertainty of height measurement.

## 18.5 Measurement method

Include:

- how volume/time was measured;
- how repeated trials were done;
- how water level change was handled;
- how temperature was measured;
- how errors were estimated.

## 18.6 Results

Include:

- raw or processed data tables;
- plots;
- fitted slopes;
- viscosity calculation;
- Reynolds numbers.

## 18.7 Discussion

Discuss:

- agreement or disagreement with theory;
- deviations for short tubes;
- possible turbulence;
- effect of tube radius uncertainty;
- comparison with literature viscosity;
- what you would improve.

## 18.8 Conclusion

State clearly:

- main measured trends;
- final viscosity value with uncertainty;
- whether Poiseuille theory was supported;
- limitations of the experiment.

## 18.9 Appendix

Include:

- full raw data;
- photos;
- video screenshots;
- extra calculations;
- calibration details.

---

# 19. Checklist for the basic level

Use this checklist before submission.

## Construction and calibration

- [ ] PET bottle device built.
- [ ] Tube diameter measured.
- [ ] Tube lengths measured.
- [ ] Tube joint sealed and leak-tested.
- [ ] Water-level marks made.
- [ ] Hydrostatic pressure calculated for each mark.
- [ ] Photos of device included.

## Measurements

- [ ] Flow measured versus pressure for one chosen tube length.
- [ ] At least 2-3 repeated trials per pressure value.
- [ ] At least 10 tube lengths measured.
- [ ] Tube lengths are between about 5 mm and 50 cm.
- [ ] Water temperature recorded.
- [ ] Start/end water heights recorded or pressure change minimized.

## Analysis

- [ ] \(Q=V/t\) calculated.
- [ ] \(v=Q/A\) calculated.
- [ ] \(\Delta p=\rho gh\) calculated.
- [ ] Plots made.
- [ ] Poiseuille prediction tested.
- [ ] Bernoulli/Torricelli comparison included.
- [ ] Reynolds number estimated.
- [ ] Viscosity of water determined.
- [ ] Uncertainty discussed.
- [ ] Conclusions supported by data.

---

# 20. Checklist for the advanced level

In addition to the basic-level checklist:

- [ ] One extra parameter study chosen.
- [ ] Extra parameter clearly stated in the abstract.
- [ ] Theoretical expectation written down before presenting data.
- [ ] Extra data measured carefully.
- [ ] Literature comparison included.
- [ ] Differences from literature discussed.
- [ ] Possible systematic errors discussed.

Recommended advanced choice: **temperature dependence of water viscosity**, because it has a clear theoretical expectation and good literature comparison.

---

# 21. Minimal calculation example

Suppose:

- tube inner radius: \(r=1.0\,\mathrm{mm}=1.0\times10^{-3}\,\mathrm{m}\);
- tube length: \(L=0.20\,\mathrm{m}\);
- water height: \(h=0.15\,\mathrm{m}\);
- collected volume: \(V=25\,\mathrm{mL}=25\times10^{-6}\,\mathrm{m^3}\);
- time: \(t=20\,\mathrm{s}\).

Pressure:

\[
\Delta p=\rho gh
=998\cdot9.81\cdot0.15
\approx1469\,\mathrm{Pa}.
\]

Flow rate:

\[
Q=\frac{V}{t}
=\frac{25\times10^{-6}}{20}
=1.25\times10^{-6}\,\mathrm{m^3/s}.
\]

Area:

\[
A=\pi r^2=\pi(10^{-3})^2=3.14\times10^{-6}\,\mathrm{m^2}.
\]

Average velocity:

\[
v=\frac{Q}{A}
=\frac{1.25\times10^{-6}}{3.14\times10^{-6}}
\approx0.40\,\mathrm{m/s}.
\]

Viscosity estimate from one point using Poiseuille:

\[
\eta=\frac{\pi r^4\Delta p}{8LQ}.
\]

Substitute:

\[
\eta
=\frac{\pi(10^{-3})^4(1469)}{8(0.20)(1.25\times10^{-6})}
\approx2.3\times10^{-3}\,\mathrm{Pa\,s}.
\]

This is higher than the expected water value near room temperature, which could indicate experimental errors, diameter error, entrance losses, non-laminar effects, or that the example numbers are not ideal. In real analysis, use many data points and a fit.

---

# 22. Suggested figures for the final report

Include at least these figures:

1. **Photo of apparatus** with labels.
2. **Calibration diagram** showing \(h\) measured from tube centerline.
3. **Calibration plot:** \(\Delta p\) versus \(h\).
4. **Flow-pressure plot:** \(Q\) versus \(\Delta p\) for one or more tube lengths.
5. **Length-dependence plot:** \(Q\) versus \(1/L\) at fixed pressure.
6. **Resistance plot:** \(R\) versus \(L\), with linear fit.
7. **Torricelli comparison:** measured \(v\) versus \(h\) compared with \(\sqrt{2gh}\).
8. **Advanced plot**, if applicable: viscosity versus temperature/concentration/liquid type.

---

# 23. Suggested wording for hypotheses

Before presenting results, write clear expectations.

Example hypotheses:

1. **Pressure hypothesis:** For sufficiently long tubes and laminar flow, the volume flow rate will be proportional to hydrostatic pressure:

\[
Q\propto\Delta p.
\]

2. **Length hypothesis:** For the same tube radius and pressure, the volume flow rate will decrease approximately inversely with tube length:

\[
Q\propto\frac{1}{L}.
\]

3. **Viscosity hypothesis:** The hydraulic resistance will increase linearly with tube length:

\[
R=\frac{\Delta p}{Q}\propto L.
\]

4. **Short-tube hypothesis:** Very short tubes may deviate from Hagen-Poiseuille theory because entrance/exit effects and ideal jet behavior become more important.

5. **Temperature hypothesis, if advanced:** Warmer water will flow faster because its viscosity is lower.

---

# 24. What makes the report strong

A strong report is not just a collection of formulas. It should show that you understand the experiment.

The strongest elements are:

- clear statement of the chosen level: basic or advanced;
- careful device documentation;
- clear calibration method;
- repeated measurements;
- uncertainty estimates;
- plots with labeled axes and units;
- comparison between Bernoulli/Torricelli and Hagen-Poiseuille theory;
- viscosity determined from a fit, not from one arbitrary point;
- honest discussion of deviations and limitations;
- raw data included in an appendix;
- photos/videos proving how measurements were done.

---

# 25. Final practical recommendation

For the cleanest experiment, do this:

1. Use one tube with a well-measured inner diameter.
2. Start long, for example 50 cm, then cut it shorter step by step.
3. Use 10 lengths between about 2 cm and 50 cm, plus maybe one very short length for comparison.
4. For each length, measure 5-8 pressure points.
5. Repeat each pressure point 2-3 times.
6. Use the volume-time method, not only projectile range.
7. Record start and end water heights.
8. Determine viscosity from the slope of \(R\) versus \(L\).
9. Use the shortest tubes mainly for discussing deviations, not for the final viscosity fit.
10. If doing advanced level, choose temperature dependence of water viscosity.

This plan should give you a report that directly addresses the assignment requirements and produces physically meaningful results.
