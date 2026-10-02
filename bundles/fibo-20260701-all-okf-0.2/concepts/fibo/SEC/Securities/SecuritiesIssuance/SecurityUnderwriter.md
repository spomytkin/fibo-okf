---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security underwriter
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that has purchased from an issuer with a view to, or sells for an issuer in connection with, the distribution
      of any security, or participates or has a direct or indirect participation in any such undertaking, or participates
      or has a participation in the direct or indirect underwriting of any such undertaking
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Section 3a of the Investment Company Act of 1940 as amended in January, 2012, https://www.sec.gov/about/laws/ica40.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N0d0ac48ac7a441d0a083a627fa31d271
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N57450f5684ba4895a3210328315af689
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: security underwriter
type: Ontology Class
---

# security underwriter

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter>

## Definition

party that has purchased from an issuer with a view to, or sells for an issuer in connection with, the distribution of any security, or participates or has a direct or indirect participation in any such undertaking, or participates or has a participation in the direct or indirect underwriting of any such undertaking

## Relationships

- **Subclass of**: [Underwriter](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)
- **Subclass of**: [ThirdPartyAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)
- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N0d0ac48ac7a441d0a083a627fa31d271`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N57450f5684ba4895a3210328315af689`

## Annotations

- **label**: security underwriter
- **definition**: party that has purchased from an issuer with a view to, or sells for an issuer in connection with, the distribution of any security, or participates or has a direct or indirect participation in any such undertaking, or participates or has a participation in the direct or indirect underwriting of any such undertaking
- **adaptedFrom**: Section 3a of the Investment Company Act of 1940 as amended in January, 2012, https://www.sec.gov/about/laws/ica40.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
