+---------------------------+
|         Customer          |
+---------------------------+
| - name: String            |
| - purchaseHistory: List   |
+---------------------------+
| + verify(): Boolean       |
+---------------------------+
          |
          | places
          v
+---------------------------+
|       Transaction         |
+---------------------------+
| - selectedItems: List     |
+---------------------------+
| + computeTotal(): Float   |
+---------------------------+
          |
          | contains (1..*)
          v
+---------------------------+
|         FoodItem          |
+---------------------------+
| - name: String            |
| - price: Float            |
| - category: String        |
| - popularityRating: Float |
+---------------------------+
+---------------------------+

+---------------------------+
|           Menu            |
+---------------------------+
| - items: List<FoodItem>   |
+---------------------------+
| + filterByCategory(       |
|     category: String)     |
|     : List<FoodItem>      |
+---------------------------+
          |
          | holds (0..*)
          v
       [FoodItem]
