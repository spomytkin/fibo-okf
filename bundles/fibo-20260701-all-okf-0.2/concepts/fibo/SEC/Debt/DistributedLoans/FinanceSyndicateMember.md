---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: finance syndicate member
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: syndicate member that is a financial services provider that contributes funds to a syndicated loan or loan participation
      note
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Syndicate members may include a variety of financial institutions, such as commercial banks, investment banks,
      institutional investors - insurance companies, pension funds, and hedge funds, and specialty finance firms, focused
      on specific industries or credit profiles, which may join syndicates for specialized or higher-risk loans.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N2cf8dc6a1d254c80b8d10f2bb8bf5bb4
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/SyndicateMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/SyndicateMember
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/FinanceSyndicateMember
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: finance syndicate member
type: Ontology Class
---

# finance syndicate member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/FinanceSyndicateMember>

## Definition

syndicate member that is a financial services provider that contributes funds to a syndicated loan or loan participation note

## Relationships

- **Subclass of**: [SyndicateMember](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/SyndicateMember.md)
- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N2cf8dc6a1d254c80b8d10f2bb8bf5bb4`

## Annotations

- **label** (en): finance syndicate member
- **definition** (en): syndicate member that is a financial services provider that contributes funds to a syndicated loan or loan participation note
- **explanatoryNote** (en): Syndicate members may include a variety of financial institutions, such as commercial banks, investment banks, institutional investors - insurance companies, pension funds, and hedge funds, and specialty finance firms, focused on specific industries or credit profiles, which may join syndicates for specialized or higher-risk loans.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
