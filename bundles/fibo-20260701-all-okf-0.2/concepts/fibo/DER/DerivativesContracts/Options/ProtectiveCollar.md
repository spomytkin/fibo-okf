---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: protective collar
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collar that consists of a covered call and protective put
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A protective collar consists of a long position in the underlying security, a put option purchased to hedge the
      downside risk on a stock, a call option written on the stock to finance the put purchase.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CoveredCall
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectivePut
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/Collar.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Collar
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectiveCollar
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: protective collar
type: Ontology Class
---

# protective collar

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ProtectiveCollar>

## Definition

collar that consists of a covered call and protective put

## Relationships

- **Subclass of**: [Collar](/concepts/fibo/DER/DerivativesContracts/Options/Collar.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [CoveredCall](/concepts/fibo/DER/DerivativesContracts/Options/CoveredCall.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [ProtectivePut](/concepts/fibo/DER/DerivativesContracts/Options/ProtectivePut.md)

## Annotations

- **label** (en): protective collar
- **definition** (en): collar that consists of a covered call and protective put
- **explanatoryNote** (en): A protective collar consists of a long position in the underlying security, a put option purchased to hedge the downside risk on a stock, a call option written on the stock to finance the put purchase.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
