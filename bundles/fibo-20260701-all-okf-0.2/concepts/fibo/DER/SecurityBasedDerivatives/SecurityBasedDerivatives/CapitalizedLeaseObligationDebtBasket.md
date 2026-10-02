---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capitalized lease obligation debt basket
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of debt instruments whose constituents are contracts entitling a renter the temporary use of an asset and,
      in accounting terms, has asset ownership characteristics
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A capitalized lease obligation basket is increasingly broadly drafted to include indebtedness incurred to finance
      the purchase, improvement, repair, renewal etc. of property (including the purchase of stock of a person owning such
      property).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N1fe0217befaa4e18b07a3ac7924e27e5
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CapitalizedLeaseObligationDebtBasket
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: capitalized lease obligation debt basket
type: Ontology Class
---

# capitalized lease obligation debt basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CapitalizedLeaseObligationDebtBasket>

## Definition

basket of debt instruments whose constituents are contracts entitling a renter the temporary use of an asset and, in accounting terms, has asset ownership characteristics

## Relationships

- **Subclass of**: [BasketOfDebtInstruments](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N1fe0217befaa4e18b07a3ac7924e27e5`

## Annotations

- **label** (en): capitalized lease obligation debt basket
- **definition** (en): basket of debt instruments whose constituents are contracts entitling a renter the temporary use of an asset and, in accounting terms, has asset ownership characteristics
- **explanatoryNote** (en): A capitalized lease obligation basket is increasingly broadly drafted to include indebtedness incurred to finance the purchase, improvement, repair, renewal etc. of property (including the purchase of stock of a person owning such property).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
