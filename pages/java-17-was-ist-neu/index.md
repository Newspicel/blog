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

Es gibt jetzt mehr Möglichkeiten Switch zu benutzen, statt if-else. Hier sind ein paar Beispiele:

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

Ich finde, das sind die wichtigsten und größten Änderungen.

### Um auch mal kurz auf die nächste Java Version zu sprechen zu kommen.
Die wichtigste Änderung für Java 18 wird die [Standardisierung von UTF-8](https://openjdk.java.net/jeps/400).

Und dann mal sehen was noch so kommt.


## Zusätzlich hat sich zum Code auch noch die Lizenz verändert. 
```Hier wurden zwei Beiträge zusammengefügt```

Am 14\. September hat Donald Smith (Sr. Director of Product Management) in einem [Blog Beitrag](https://blogs.oracle.com/java-platform-group/faster-and-easier-use-and-redistribution-of-java-se) vorgestellt, das die Lizenz von OracleJDK nun [Oracle No-Fee](https://www.oracle.com/downloads/licenses/no-fee-license.html) steht.

Diese kostenlose Lizenz umfasst das JDK und die vierteljährlichen Sicherheitsupdates auch für die kommerzielle und produktive Nutzung. Die neue Lizenz ist die "Oracle No-Fee Terms and Conditions"-Lizenz (NFTC) und erlaubt die kostenlose Nutzung für alle Benutzer, auch für die kommerzielle und produktive Nutzung. Die Weiterverbreitung ist erlaubt, solange sie nicht kostenpflichtig ist.

Frühere Versionen sind von dieser Änderung nicht betroffen. Oracle wird weiterhin Oracle OpenJDK-Releases unter der GPL nach denselben Releases und demselben Zeitplan wie seit Java 9 bereitstellen.

Es gibt weiterhin die kostenpflichtige Version, ich glaube aber nicht, dass sie einen von uns interessiert.

Happy End: Nun können wir uns die Java Version ohne das lästige Durchklicken herunterladen. Oder einfach bei der [OpenJDK](https://openjdk.java.net/) oder [SDKMan](https://sdkman.io/) bleiben.



	
