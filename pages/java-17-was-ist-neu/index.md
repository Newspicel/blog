# Java 17 - Was ist neu ?
<!-- date: 2021-09-21 11:58:00 -->
<!-- category: java -->
<!-- description: Die neue Java LTS ist draußen. Also kann man sich die Frage stellen: Was ist neu? -->
Die neue Java LTS ist draußen. Also kann man sich die Frage stellen: Was ist neu? 

* [Pattern Matching for switch](https://openjdk.java.net/jeps/406)
* [Sealed Classes](https://openjdk.java.net/jeps/409)
* [Vector API](https://openjdk.java.net/jeps/414)
* Wie immer wurden wieder alte APIs entfernt.
* Weiteres zum selber nachlesen: [OpenJDK17](https://openjdk.java.net/projects/jdk/17/)


Das finde ich sind die wichtigsten Sachen, die sich verändert haben.

Um kurz auch mal über Pattern Matching für Switch und Sealed Classes zu reden:

#### Pattern Matching:

Es gibt jetzt mehr möglichkeiten Switch zu benutzen, statt if-else. Hier sind ein paar Bespiele:

```java
static void testTriangle(Shape s) {
    switch (s) {
        case Triangle t && (t.calculateArea() > 100) ->
            System.out.println("Large triangle");
        default ->
            System.out.println("A shape, possibly a small triangle");
    }
}
```


```java
static void test(Object o) {
    switch (o) {
        case null      -> throw new NullPointerException();
        case String s  -> System.out.println("String: "+s);
        case Integer i -> System.out.println("Integer");
        default  -> System.out.println("default");
    }
}
```

#### Sealed Classes:

Man kann nun einschränken, wer alles eine Klasse erben oder implementieren kann.

```java
public abstract sealed class Shape
    permits Circle, Rectangle, Square { ... }
```


## Was wurde zwischen der letzter LTS Version und jetzt verändert?

* [Pattern Matching for switch](https://openjdk.java.net/jeps/406)
* [Sealed Classes](https://openjdk.java.net/jeps/409)
* [Records](https://openjdk.java.net/jeps/395)
* [Migrate to GitHub](https://openjdk.java.net/jeps/369)
* [Text Blocks](https://openjdk.java.net/jeps/378)
* [Pattern Matching for instanceof](https://openjdk.java.net/jeps/305)
* [Switch Expressions](https://openjdk.java.net/jeps/361)

Das finde, ich sind die wichtigsten und größten Änderungen.

### Um auch mal kurz auf die nächste Java Version zu sprechen zu kommen.
In Java 18 ist das wichtigste was geplannt ist, das [UTF-8 dann Standart](https://openjdk.java.net/jeps/400) wird. 

Und dann mal sehen was noch so kommt.



	
