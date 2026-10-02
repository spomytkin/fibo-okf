---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call put warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that either does not specify call or put features, or that explicitly includes both a call and put feature
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The call and put code, 'B', in the CFI stands for 'Both', meaning such a warrant embodies characteristics of both
      a call and a put. This can appear in structured warrants or exotic warrants where payout may depend on movements in
      either direction (or give the holder a choice at certain triggers).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: straddle warrant
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/CallWarrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallWarrant
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/PutWarrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/PutWarrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallPutWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: call put warrant
type: Ontology Class
---

# call put warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CallPutWarrant>

## Definition

warrant that either does not specify call or put features, or that explicitly includes both a call and put feature

## Relationships

- **Subclass of**: [CallWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/CallWarrant.md)
- **Subclass of**: [PutWarrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/PutWarrant.md)

## Annotations

- **label** (en): call put warrant
- **definition** (en): warrant that either does not specify call or put features, or that explicitly includes both a call and put feature
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): The call and put code, 'B', in the CFI stands for 'Both', meaning such a warrant embodies characteristics of both a call and a put. This can appear in structured warrants or exotic warrants where payout may depend on movements in either direction (or give the holder a choice at certain triggers).
- **synonym** (en): straddle warrant

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
