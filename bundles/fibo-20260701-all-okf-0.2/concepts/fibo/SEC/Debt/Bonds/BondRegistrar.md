---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond registrar
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party responsible for maintaining records on behalf of the issuer that identify the owners of a registered bond
      issue
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The trustee under a bond contract often also acts as registrar.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/registers
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registrar
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondRegistrar
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond registrar
type: Ontology Class
---

# bond registrar

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondRegistrar>

## Definition

party responsible for maintaining records on behalf of the issuer that identify the owners of a registered bond issue

## Relationships

- **Subclass of**: [LegalAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- **Subclass of**: [Registrar](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registrar>)

## Constraints

- **[registers](<https://www.omg.org/spec/Commons/RegistrationAuthorities/registers>)**: some values from of type [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Annotations

- **label**: bond registrar
- **definition**: party responsible for maintaining records on behalf of the issuer that identify the owners of a registered bond issue
- **explanatoryNote**: The trustee under a bond contract often also acts as registrar.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
