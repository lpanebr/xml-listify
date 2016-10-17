# xml-listify
Converts a tabbed text into XML `<list>` / `<list-item>`

Sample input:

```html
<p>1. Arborescent plants (tree ferns)</p>
	<p>2. Petiole base with black</p>
		<p>3. Aphlebias present ......... <italic>Alsophila setosa</italic></p>
		<p>3. Aphlebias absent ......... <italic>Alsophila sternbergii</italic></p>
	<p>2. Petiole base with spines</p>
		<p>4. Petiole scales whitish or bicolor</p>
			<p>5. Petiole base deciduous ......... <italic>Cyathea hirsuta</italic></p>
			<p>5. Petiole base persistent on the stem, scales without setae</p>
				<p>6. Petiole scales concolor (whitish) ......... <italic>Cyathea leucofolis</italic></p>
				<p>6. Petiole scales bicolor (whitish and brown) ......... <italic>Cyathea dichromatolepis</italic></p>
		<p>4. Petiole scales brown</p>
			<p>7. Petiole base deciduous leaving a scar on the stem, indusium globose ......... <italic>Cyathea delgadii</italic></p>
			<p>7. Petiole base persistent on the stem, indusium absent</p>
				<p>8. Secondary veins predominantly forked ......... <italic>Cyathea phalerata</italic></p>
				<p>8. Secondary veins predominantly simple</p>
					<p>9. Petiole with spines at base ......... <italic>Cyathea atrovirens</italic></p>
					<p>9. Petiole without spines ......... <italic>Cyathea glaziovii</italic></p>
```

Sample output:
```xml
<list list-type="simple">
    <list-item><p>1. Arborescent plants (tree ferns)</p></list-item>
    <list-item>
        <list list-type="simple">
            <list-item><p>2. Petiole base with black</p></list-item>
            <list-item>
                <list list-type="simple">
                    <list-item><p>3. Aphlebias present ......... <italic>Alsophila setosa</italic></p></list-item>
                    <list-item><p>3. Aphlebias absent ......... <italic>Alsophila sternbergii</italic></p></list-item>
                </list>
            </list-item>
            <list-item><p>2. Petiole base with spines</p></list-item>
            <list-item>
                <list list-type="simple">
                    <list-item><p>4. Petiole scales whitish or bicolor</p></list-item>
                    <list-item>
                        <list list-type="simple">
                            <list-item><p>5. Petiole base deciduous ......... <italic>Cyathea hirsuta</italic></p></list-item>
                            <list-item><p>5. Petiole base persistent on the stem, scales without setae</p></list-item>
                            <list-item>
                                <list list-type="simple">
                                    <list-item><p>6. Petiole scales concolor (whitish) ......... <italic>Cyathea leucofolis</italic></p></list-item>
                                    <list-item><p>6. Petiole scales bicolor (whitish and brown) ......... <italic>Cyathea dichromatolepis</italic></p></list-item>
                                </list>
                            </list-item>
                        </list>
                    </list-item>
                    <list-item><p>4. Petiole scales brown</p></list-item>
                    <list-item>
                        <list list-type="simple">
                            <list-item><p>7. Petiole base deciduous leaving a scar on the stem, indusium globose ......... <italic>Cyathea delgadii</italic></p></list-item>
                            <list-item><p>7. Petiole base persistent on the stem, indusium absent</p></list-item>
                            <list-item>
                                <list list-type="simple">
                                    <list-item><p>8. Secondary veins predominantly forked ......... <italic>Cyathea phalerata</italic></p></list-item>
                                    <list-item><p>8. Secondary veins predominantly simple</p></list-item>
                                    <list-item>
                                        <list list-type="simple">
                                            <list-item><p>9. Petiole with spines at base ......... <italic>Cyathea atrovirens</italic></p></list-item>
                                            <list-item><p>9. Petiole without spines ......... <italic>Cyathea glaziovii</italic></p></list-item>
                                        </list>
                                    </list-item>
                                </list>
                            </list-item>
                        </list>
                    </list-item>
                </list>
            </list-item>
        </list>
    </list-item>
</list>
```
