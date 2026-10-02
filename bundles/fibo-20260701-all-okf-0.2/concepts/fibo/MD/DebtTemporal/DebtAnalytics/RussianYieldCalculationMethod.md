---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: russian yield calculation method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The method used in determining Yield in the Russian markets. This is based on an effective yield with fundamentally
      different math. To give an example of the use of a different "yield type", we have Russia, which trades based on an
      effective yield. The price-yield math is fundamentally different. Notes Origin:Fidessa Uses a trade space and effective
      yield formula. MAy have same day types but different math.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RussianYieldFormula
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasFormula
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RussianYieldCalculationMethod
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: russian yield calculation method
type: Ontology Class
---

# russian yield calculation method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RussianYieldCalculationMethod>

## Definition

The method used in determining Yield in the Russian markets. This is based on an effective yield with fundamentally different math. To give an example of the use of a different "yield type", we have Russia, which trades based on an effective yield. The price-yield math is fundamentally different. Notes Origin:Fidessa Uses a trade space and effective yield formula. MAy have same day types but different math.

## Relationships

- **Subclass of**: [YieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)

## Constraints

- **[hasFormula](/concepts/fibo/FND/Utilities/Analytics/hasFormula.md)**: some values from of type [RussianYieldFormula](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/RussianYieldFormula.md)

## Annotations

- **label** (en): russian yield calculation method
- **definition** (en): The method used in determining Yield in the Russian markets. This is based on an effective yield with fundamentally different math. To give an example of the use of a different "yield type", we have Russia, which trades based on an effective yield. The price-yield math is fundamentally different. Notes Origin:Fidessa Uses a trade space and effective yield formula. MAy have same day types but different math.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
