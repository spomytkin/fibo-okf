---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency m b s issuer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The issuer of the pass through MBS is an Agency issuer. This is identified as being some kind of agency that is
      set up specifically to issue these instruments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/GovernmentMortgageAgency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/GovernmentMortgageAgency
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MBSIssuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSIssuer
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSIssuer
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: agency m b s issuer
type: Ontology Class
---

# agency m b s issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSIssuer>

## Definition

The issuer of the pass through MBS is an Agency issuer. This is identified as being some kind of agency that is set up specifically to issue these instruments.

## Relationships

- **Subclass of**: [GovernmentMortgageAgency](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/GovernmentMortgageAgency.md)
- **Subclass of**: [MBSIssuer](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MBSIssuer.md)

## Annotations

- **label** (en): agency m b s issuer
- **definition** (en): The issuer of the pass through MBS is an Agency issuer. This is identified as being some kind of agency that is set up specifically to issue these instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
