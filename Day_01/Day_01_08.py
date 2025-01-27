# Exercise 8:Widgets and Gizmos

widgets_w = 75
gizmo_w = 112

widgets = int(input("Enter the number of widgets : "))
gizmos = int(input("Enter the number of gizmos : "))

total_weight = ((widgets*widgets_w) + (gizmos*gizmo_w))/1000
print("The total weight is %.2f kg"%total_weight)