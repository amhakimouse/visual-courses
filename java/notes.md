**`@AllArgsConstructor`** is a Lombok annotation used in Java to ==automatically generate a constructor with one parameter for every field in your class==

```java
import lombok.AllArgsConstructor;
import lombok.Data; // Génère getters, setters, toString, equals et hashCode

@Data
@AllArgsConstructor
public class User {
    private Long id;
    private String name;
    private String email;
}
```

### redefinir la methode equals:

```java
import java.util.Objects;
    @Override
    public boolean equals(Object o) {                                  
        if (o == null || !(o instanceof Vol))
            return false;
        Vol autre = (Vol) o;                        
        return numVol.equals(autre.numVol);          
    }
    @Override
    public int hashcode(){
        return this.numVol.hashcode();
    }
```

| Symbol | Visibility        |
| ------ | ----------------- |
| **+**  | **Public**        |
| `-`    | Private           |
| `#`    | Protected         |
| `~`    | Package / Default |
