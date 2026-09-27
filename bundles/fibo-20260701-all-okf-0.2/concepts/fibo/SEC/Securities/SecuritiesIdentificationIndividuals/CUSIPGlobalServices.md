---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CUSIP Global Services
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: CUSIP Global Services financial services provider that is the national numbering agency (NNA) for CUSIPs in North
      America
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobalInc-US-NY.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobalInc-US-NY
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.cusip.com/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: CUSIP Global Services
type: Ontology Individual
---

# CUSIP Global Services

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices>

## Definition

CUSIP Global Services financial services provider that is the national numbering agency (NNA) for CUSIPs in North America

## Relationships

- **Related to**: [SPGlobalInc-US-NY](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SPGlobalInc-US-NY.md)
- **See also**: [http://www.cusip.com/](<http://www.cusip.com/>)

## Annotations

- **label**: CUSIP Global Services
- **definition**: CUSIP Global Services financial services provider that is the national numbering agency (NNA) for CUSIPs in North America

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
