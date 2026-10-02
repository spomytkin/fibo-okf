---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency m b s deal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An issue of securities backed by pools of mortgages held by government agencies.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These are Ginnie Mae, Freddie Mac and Fannie Mae (for the US). Of these agencies, GNMA (Ginnie Mae) issues mortgages
      in its own right (Investorwords differs on this). Fannie Mae and Freddie Mac purchase mortgages. Those mortgages are
      issued by banks. Before one of these agencies purchases a mortgage, there are certain criteria that have to be met.
      These are specified in terms of, for example, the balance of the mortgage, limits to credit ratings.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/PrivateLabelMBSDeal.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PrivateLabelMBSDeal
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSDeal
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: agency m b s deal
type: Ontology Class
---

# agency m b s deal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSDeal>

## Definition

An issue of securities backed by pools of mortgages held by government agencies.

## Relationships

- **Subclass of**: [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)

## Constraints

- **Disjoint with**: [PrivateLabelMBSDeal](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/PrivateLabelMBSDeal.md)

## Annotations

- **label** (en): agency m b s deal
- **definition** (en): An issue of securities backed by pools of mortgages held by government agencies.
- **explanatoryNote** (en): These are Ginnie Mae, Freddie Mac and Fannie Mae (for the US). Of these agencies, GNMA (Ginnie Mae) issues mortgages in its own right (Investorwords differs on this). Fannie Mae and Freddie Mac purchase mortgages. Those mortgages are issued by banks. Before one of these agencies purchases a mortgage, there are certain criteria that have to be met. These are specified in terms of, for example, the balance of the mortgage, limits to credit ratings.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
