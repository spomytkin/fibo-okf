---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bloomberg L.P.
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Bloomberg L.P. functional entity, which is a global business and financial information services and news provider
      as well as a FIGI registration authority
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP-US-DE.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP-US-DE
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry.md
    predicate: https://www.omg.org/spec/Commons/Organizations/manages
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Bloomberg L.P.
type: Ontology Individual
---

# Bloomberg L.P.

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP>

## Definition

Bloomberg L.P. functional entity, which is a global business and financial information services and news provider as well as a FIGI registration authority

## Relationships

- **Related to**: [FinancialInstrumentGlobalIdentifierRegistry](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry.md)
- **Related to**: [BloombergLP-US-DE](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP-US-DE.md)

## Annotations

- **label**: Bloomberg L.P.
- **definition**: Bloomberg L.P. functional entity, which is a global business and financial information services and news provider as well as a FIGI registration authority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
