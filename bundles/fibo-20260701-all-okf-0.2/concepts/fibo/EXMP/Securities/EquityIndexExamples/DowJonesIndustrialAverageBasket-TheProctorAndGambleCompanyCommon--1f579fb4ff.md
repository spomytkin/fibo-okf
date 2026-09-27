---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Dow Jones Industrial Average basket - The Proctor & Gamble Company common stock constituent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The Proctor & Gamble Company common stock constituent of the DJIA basket of 30 stocks
  - datatype: http://www.w3.org/2001/XMLSchema#decimal
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasWeight
    value: '1.0'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/SecuritiesBasketConstituent
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/XNYSListedTheProctorAndGambleCompanyCommonStock.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/involves
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNYSListedTheProctorAndGambleCompanyCommonStock
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket.md
    predicate: https://www.omg.org/spec/Commons/Collections/isConstituentOf
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket
  - concept: /concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket-TheProctorAndGambleCompanyCommon--6aab28f2fb.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasDateAdded
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket-TheProctorAndGambleCompanyCommonStockDateAdded
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket-TheProctorAndGambleCompanyCommonStockConstituent
sources:
- id: fibo-source-c9fb5c672c
  resource: references/fibo/EXMP/Securities/EquityIndexExamples.rdf
  sha256: c9fb5c672cbb6dc4ba551074dd33b7e27294259b5a24a6064670bc5c0205149d
  title: FIBO source EXMP/Securities/EquityIndexExamples.rdf
title: Dow Jones Industrial Average basket - The Proctor & Gamble Company common stock constituent
type: Ontology Individual
---

# Dow Jones Industrial Average basket - The Proctor & Gamble Company common stock constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket-TheProctorAndGambleCompanyCommonStockConstituent>

## Definition

The Proctor & Gamble Company common stock constituent of the DJIA basket of 30 stocks

## Relationships

- **Related to**: [DowJonesIndustrialAverageBasket-TheProctorAndGambleCompanyCommonStockDateAdded](/concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket-TheProctorAndGambleCompanyCommon--6aab28f2fb.md)
- **Related to**: [XNYSListedTheProctorAndGambleCompanyCommonStock](/concepts/fibo/EXMP/Securities/EquitiesExamples/XNYSListedTheProctorAndGambleCompanyCommonStock.md)
- **Related to**: [DowJonesIndustrialAverageBasket](/concepts/fibo/EXMP/Securities/EquityIndexExamples/DowJonesIndustrialAverageBasket.md)

## Annotations

- **label**: Dow Jones Industrial Average basket - The Proctor & Gamble Company common stock constituent
- **definition**: The Proctor & Gamble Company common stock constituent of the DJIA basket of 30 stocks
- **hasWeight**: 1.0

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
