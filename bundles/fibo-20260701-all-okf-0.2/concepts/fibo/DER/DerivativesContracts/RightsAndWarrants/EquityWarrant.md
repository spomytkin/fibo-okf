---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that permits the holder to acquire a specified amount of an equity instrument during a specified period
      at a specified price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An equity warrant typically enables a buyer to purchase shares of capital stock issued by the corporation whose
      equity is the underlying asset.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: company warrant
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: N607aa29c695643b3a5a36fd2a732de1b
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.lawinsider.com/dictionary/company-warrant
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/CallWarrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallWarrant
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/TraditionalWarrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/TraditionalWarrant
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/EquityWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: equity warrant
type: Ontology Class
---

# equity warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/EquityWarrant>

## Definition

warrant that permits the holder to acquire a specified amount of an equity instrument during a specified period at a specified price

## Relationships

- **See also**: [company-warrant](<https://www.lawinsider.com/dictionary/company-warrant>)
- **Subclass of**: [CallWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/CallWarrant.md)
- **Subclass of**: [TraditionalWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/TraditionalWarrant.md)
- **Subclass of**: [EquityDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `N607aa29c695643b3a5a36fd2a732de1b`

## Annotations

- **label** (en): equity warrant
- **definition** (en): warrant that permits the holder to acquire a specified amount of an equity instrument during a specified period at a specified price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): An equity warrant typically enables a buyer to purchase shares of capital stock issued by the corporation whose equity is the underlying asset.
- **synonym** (en): company warrant

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
