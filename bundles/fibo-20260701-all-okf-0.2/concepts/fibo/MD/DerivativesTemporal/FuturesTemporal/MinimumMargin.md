---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minimum margin
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The lowest amount an account can reach before needing to be replenished.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/MinimumMargin
sources:
- id: fibo-source-c2e233cb71
  resource: references/fibo/MD/DerivativesTemporal/FuturesTemporal.rdf
  sha256: c2e233cb71a6057762c1da19bf2b1316166cd651fcf570e55af51b91c70f41c5
  title: FIBO source MD/DerivativesTemporal/FuturesTemporal.rdf
title: minimum margin
type: Ontology Class
---

# minimum margin

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/MinimumMargin>

## Definition

The lowest amount an account can reach before needing to be replenished.

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Constraints

- **[hasAsOfDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAsOfDate.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: some values from of type [FuturesTradingAccountHolder](/concepts/fibo/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder.md)

## Annotations

- **label** (en): minimum margin
- **definition** (en): The lowest amount an account can reach before needing to be replenished.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
