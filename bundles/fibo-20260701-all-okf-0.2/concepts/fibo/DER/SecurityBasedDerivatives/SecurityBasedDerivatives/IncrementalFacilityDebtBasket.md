---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: incremental facility debt basket
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of credit facilities whose constituents are extensible, allowing companies to borrow an additional term
      loan or revolving credit facility (or increase the commitments applicable thereto) under the same credit agreement subject
      to certain parameters
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The incremental debt basket is available to borrowers and guarantors only; it cannot be used by non-guarantor entities
      to raise indebtedness. The size of the incremental debt basket varies depending on the size and creditworthiness of
      the credit group. The principle of a basket consists of allowing the borrower, up to a maximum determined amount, to
      make restricted payments, disposals or investments, or take on incremental debt. Commonly, a basket is expressed as
      subject to restrictions based on a fixed ('hard cap') amount (e.g., may not exceed EUR 5,000,000).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: builder basket
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/IncrementalFacilityDebtBasket
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: incremental facility debt basket
type: Ontology Class
---

# incremental facility debt basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/IncrementalFacilityDebtBasket>

## Definition

basket of credit facilities whose constituents are extensible, allowing companies to borrow an additional term loan or revolving credit facility (or increase the commitments applicable thereto) under the same credit agreement subject to certain parameters

## Relationships

- **Subclass of**: [CreditFacilityDebtBasket](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket.md)

## Annotations

- **label** (en): incremental facility debt basket
- **definition** (en): basket of credit facilities whose constituents are extensible, allowing companies to borrow an additional term loan or revolving credit facility (or increase the commitments applicable thereto) under the same credit agreement subject to certain parameters
- **explanatoryNote** (en): The incremental debt basket is available to borrowers and guarantors only; it cannot be used by non-guarantor entities to raise indebtedness. The size of the incremental debt basket varies depending on the size and creditworthiness of the credit group. The principle of a basket consists of allowing the borrower, up to a maximum determined amount, to make restricted payments, disposals or investments, or take on incremental debt. Commonly, a basket is expressed as subject to restrictions based on a fixed ('hard cap') amount (e.g., may not exceed EUR 5,000,000).
- **synonym** (en): builder basket

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
