---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has original issue discount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: discount from par value at the time a bond or other debt instrument is issued
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The OID is the difference between the stated redemption price at maturity and the actual issue price.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondOffering
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/hasOriginalIssueDiscount
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: has original issue discount
type: Ontology Property
---

# has original issue discount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/hasOriginalIssueDiscount>

## Definition

discount from par value at the time a bond or other debt instrument is issued

## Relationships

- **Domain**: [BondOffering](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md)
- **Range**: [Percentage](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage>)

## Annotations

- **label** (en): has original issue discount
- **definition** (en): discount from par value at the time a bond or other debt instrument is issued
- **explanatoryNote** (en): The OID is the difference between the stated redemption price at maturity and the actual issue price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
