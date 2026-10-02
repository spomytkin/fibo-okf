---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Global Legal Entity Identifier Foundation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Global Legal Entity Identifier Foundation (GLEIF) legal entity, tasked to support the implementation and use of
      the Legal Entity Identifier (LEI)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Global Legal Entity Identifier Foundation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GLEIF
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.gleif.org/en/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundationAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundationAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundationAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundationAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundation
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: Global Legal Entity Identifier Foundation
type: Ontology Individual
---

# Global Legal Entity Identifier Foundation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundation>

## Definition

Global Legal Entity Identifier Foundation (GLEIF) legal entity, tasked to support the implementation and use of the Legal Entity Identifier (LEI)

## Relationships

- **Related to**: [GlobalLegalEntityIdentifierFoundationAddress](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundationAddress.md)
- **Related to**: [GlobalLegalEntityIdentifierFoundationAddress](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GlobalLegalEntityIdentifierFoundationAddress.md)

## Annotations

- **label**: Global Legal Entity Identifier Foundation
- **definition**: Global Legal Entity Identifier Foundation (GLEIF) legal entity, tasked to support the implementation and use of the Legal Entity Identifier (LEI)
- **hasLegalName**: Global Legal Entity Identifier Foundation
- **abbreviation**: GLEIF
- **hasWebsite**: https://www.gleif.org/en/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
