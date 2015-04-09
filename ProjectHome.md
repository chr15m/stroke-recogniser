Small Python library to recognise and classify strokes of the pen or mouse gestures according to their shape.

Can detect single pen strokes or gestures. Override the 'alphabet' variable to add your own strokes to be recognised. The example below shows how far away different candidate letters are from the test stroke.

```
>>> g = StrokeRecogniser()
>>> g.PenDown((100, 100))
>>> g.PenTo((80, 80))
>>> g.PenTo((50, 100))
>>> g.PenTo((40, 150))
>>> g.PenTo((55, 190))
>>> g.PenTo((75, 210))
>>> print g.PenUp((98, 200))
[('C', 1.2624129937734025), ('E', 1.5851903448074731), ('Q', 2.6428733986175001), ('G', 3.9534192455350494), ('K', 3.9840480311640869)]
```

An example for learning new strokes is also included.